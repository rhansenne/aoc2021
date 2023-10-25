import copy
map=[list(row.strip()) for row in open('input.txt', 'r').readlines()]

def step():
    global map
    moved=False
    nextmap=copy.deepcopy(map)
    for rowid, row in enumerate(map):
        for colid, val in enumerate(row):
            nextcolid = 0 if colid+1==len(row) else colid+1
            if val=='>' and row[nextcolid]=='.':
                nextmap[rowid][colid]='.'
                nextmap[rowid][nextcolid]='>'
                moved=True
    map=nextmap
    nextmap=copy.deepcopy(map)
    for rowid, row in enumerate(map):
        nextrowid = 0 if rowid+1==len(map) else rowid+1
        for colid, val in enumerate(row):
            if val=='v' and map[nextrowid][colid]=='.':
                nextmap[rowid][colid]='.'
                nextmap[nextrowid][colid]='v'
                moved=True
    map=nextmap
    return moved

i=1
while True:
    if not step():
        print(i)
        exit()
    i+=1