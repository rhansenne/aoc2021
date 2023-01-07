max_x=0
max_y=0
holes=set()
instructions=[]
for line in open('input.txt', 'r').readlines():
    if len(line)==1:
        continue
    if 'fold' in line:
        instructions.append(line.strip())
        continue
    co = tuple(int(n) for n in line.strip().split(','))
    if co[0]>max_x:
        max_x=co[0]
    if co[1]>max_y:
        max_y=co[1]
    holes.add(co)
paper=[[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
for hole in holes:
    paper[hole[1]][hole[0]]=1
instruction=instructions[0]
fold=int(instruction.split('=')[1])
if "y=" in instruction:
    for y in range(fold,len(paper)):
        for x in range(0,len(paper[0])):
            if paper[y][x]==1:
                paper[2*fold-y][x]=1
    paper=[paper[y] for y in range(0,fold)]
else: 
    for y in range(0,len(paper)):
        for x in range(fold,len(paper[0])):
            if paper[y][x]==1:
                paper[y][2*fold-x]=1
    paper=[[y[x] for x in range(0,fold)] for y in paper]                
print(sum([sum(i) for i in paper]))
