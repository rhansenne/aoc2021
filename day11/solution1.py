octos = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]

def neighbours(i,j):
    nb=set()
    if i>0:
        nb.add((i-1,j))
        if j>0:
            nb.add((i-1,j-1))
        if j<len(octos[0])-1:
            nb.add((i-1,j+1))
    if i<len(octos)-1:
        nb.add((i+1,j))
        if j>0:
            nb.add((i+1,j-1))
        if j<len(octos[0])-1:
            nb.add((i+1,j+1))
    if j>0:
        nb.add((i,j-1))
    if j<len(octos[0])-1:
        nb.add((i,j+1))
    return nb

def check_flash(flashed,i,j):
    if octos[i][j]>9 and (i,j) not in flashed:
        flashed.add((i,j))
        for nb in neighbours(i,j):
            octos[nb[0]][nb[1]]+=1
            check_flash(flashed,nb[0],nb[1])

flashes=0
for step in range(0,100): 
    flashed=set()
    for i in range(0,len(octos)):
        for j in range(0,len(octos[0])):
            octos[i][j]+=1
    for i in range(0,len(octos)):
        for j in range(0,len(octos[0])):
            check_flash(flashed,i,j)
    for co in flashed:
        octos[co[0]][co[1]]=0
    flashes+=len(flashed)
print(flashes)