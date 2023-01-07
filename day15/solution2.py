from dijkstar import Graph, find_path
import math

cave = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]
cave_25x = [[0 for i in range(len(cave)*5)] for j in range(len(cave[0])*5)]
for i in range(len(cave)*5):
    repx=math.floor(i/len(cave))
    for j in range(len(cave[0])*5):
        repy=math.floor(j/len(cave[0]))
        cave_25x[i][j] = cave[i%len(cave)][j%len(cave[0])]+repx+repy
        if (cave_25x[i][j]>9):
            cave_25x[i][j]-=9
graph = Graph()
for i in range(len(cave_25x)-1):
    for j in range(len(cave_25x[0])):
        graph.add_edge((i,j),(i+1,j), cave_25x[i+1][j])
        graph.add_edge((i+1,j),(i,j), cave_25x[i][j])
for i in range(len(cave_25x)):
    for j in range(len(cave_25x[0])-1):
        graph.add_edge((i,j),(i,j+1), cave_25x[i][j+1])
        graph.add_edge((i,j+1),(i,j), cave_25x[i][j])
print(find_path(graph, (0,0), (len(cave_25x)-1,len(cave_25x[0])-1)).total_cost)