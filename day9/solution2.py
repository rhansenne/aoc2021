heightmap = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]

def expand(basin,i,j):
    basin.add((i,j))
    if i>0 and heightmap[i-1][j]<9 and (i-1,j) not in basin:
        expand(basin,i-1,j)
    if i<len(heightmap)-1 and heightmap[i+1][j]<9 and (i+1,j) not in basin:
        expand(basin,i+1,j)
    if j>0 and heightmap[i][j-1]<9 and (i,j-1) not in basin:
        expand(basin,i,j-1)
    if j<len(heightmap[0])-1 and heightmap[i][j+1]<9 and (i,j+1) not in basin:
        expand(basin,i,j+1)
    return basin

sizes=[]
for i in range(0,len(heightmap)):
    for j in range(0,len(heightmap[0])):
        if (i==0 or heightmap[i][j] < heightmap[i-1][j]) \
        and (i==len(heightmap)-1 or heightmap[i][j] < heightmap[i+1][j]) \
        and (j==0 or heightmap[i][j] < heightmap[i][j-1]) \
        and (j==len(heightmap[0])-1 or heightmap[i][j] < heightmap[i][j+1]):
            sizes.append(len(expand(set(),i,j)))  
sizes.sort(reverse=True)
print(sizes[0]*sizes[1]*sizes[2])
