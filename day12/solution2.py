count=0
vertices={}    

class vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors=set()
    def __repr__(self):
        return self.name

def explore(vertex,visited,visited_twice):
    global count
    visited.append(vertex)
    for v in vertex.neighbors:
        if v.name == 'start':
            continue
        if v.name == 'end':
            count+=1
        elif v.name.isupper() or v not in visited:
            explore(v,visited.copy(),visited_twice)
        elif not visited_twice:
            explore(v,visited.copy(),True)

def getVertex(name):
    if name not in vertices:
        vertices[name]=vertex(name)
    return vertices[name]

for line in open('input.txt', 'r').readlines():
    edge = line.strip().split('-')
    v1 = getVertex(edge[0])
    v2 = getVertex(edge[1])
    v1.neighbors.add(v2)
    v2.neighbors.add(v1)
    if v1.name == 'start':
        start = v1
explore(start,[],False)
print(count)