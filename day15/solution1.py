from dijkstar import Graph, find_path

cave = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]
graph = Graph()
for i in range(len(cave)-1):
    for j in range(len(cave[0])):
        graph.add_edge((i,j),(i+1,j), cave[i+1][j])
        graph.add_edge((i+1,j),(i,j), cave[i][j])
for i in range(len(cave)):
    for j in range(len(cave[0])-1):
        graph.add_edge((i,j),(i,j+1), cave[i][j+1])
        graph.add_edge((i,j+1),(i,j), cave[i][j])
print(find_path(graph, (0,0), (len(cave)-1,len(cave[0])-1)).total_cost)