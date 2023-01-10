from dijkstar import Graph, find_path
from statistics import mode

def normalize(co,perm_axis,perm_dir):
    return (perm_dir[0]*co[perm_axis[0]],perm_dir[1]*co[perm_axis[1]],perm_dir[2]*co[perm_axis[2]])

def denormalize(co,perm_axis,perm_dir):
    co0=co1=co2=-1
    for i in range(len(perm_axis)):
        match perm_axis[i]:
            case 0: co0=i
            case 1: co1=i
            case 2: co2=i
    return (perm_dir[co0]*co[co0],perm_dir[co1]*co[co1],perm_dir[co2]*co[co2])

#print('no',normalize((11,22,33),(2, 0, 1), (1, -1, -1)))
#print('deno', denormalize(  normalize((11,22,33),(2, 0, 1), (1, -1, -1)) ,(2, 0, 1), (1, -1, -1) )  )

report=[]
for line in open('input.txt', 'r').readlines():
    if 'scanner' in line:
        report.append([])
    if ',' in line:
        report[len(report)-1].append(tuple(int(pos) for pos in line.split(',')))

overlap_graph = Graph()
transforms={}
for i in range(len(report)):
    for j in range (i+1,len(report)):
        diffs=[]
        for iscan in report[i]:
            for jscan in report[j]:
                 for perm_axis in ((0,1,2),(0,2,1),(1,0,2),(2,0,1),(1,2,0),(2,1,0)):
                    for perm_dir in ((1,1,1),(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,1),(-1,1,-1),(1,-1,-1),(-1,-1,-1)):
                         diff=(iscan[0]-perm_dir[0]*jscan[perm_axis[0]],iscan[1]-perm_dir[1]*jscan[perm_axis[1]],iscan[2]-perm_dir[2]*jscan[perm_axis[2]])
                         diffs.append((diff,perm_axis,perm_dir))
        most_freq = mode(diffs)
        if diffs.count(most_freq) >= 12: #scans overlap
            overlap_graph.add_edge(i,j,1)
            overlap_graph.add_edge(j,i,1)
            print('overlap',i,j,'transform:',most_freq)
            transforms[(i,j)]=most_freq
#print(transforms)

beacons=set()
for j in range(len(report)):
    print('REPORT',j)
    path = find_path(overlap_graph, j, 0).nodes
    print(path)
    for p in range(len(path)):
        if path[p]==0:
            beacons.update(report[j])
        else: #transform coordinates
            print('checking for',(path[p+1],path[p]))
            if (path[p+1],path[p]) in transforms:
                print('normalize')
                tr=transforms[(path[p+1],path[p])]
                for c in range(len(report[j])):
                    norm_coord = normalize(report[j][c],tr[1],tr[2])
                    report[j][c]= (norm_coord[0]+tr[0][0],norm_coord[1]+tr[0][1],norm_coord[2]+tr[0][2])
            else:
                print('denormalize')
                tr=transforms[(path[p],path[p+1])]
                for c in range(len(report[j])):
                    norm_coord = denormalize(report[j][c],tr[1],tr[2])
                    norm_tr=denormalize(tr[0],tr[1],tr[2])
                    report[j][c]= (norm_coord[0]-norm_tr[0],norm_coord[1]-norm_tr[1],norm_coord[2]-norm_tr[2])
print(len(beacons))


#for r in report:
#    print('REPORT',r)
#    for c in r:
#        print(c)