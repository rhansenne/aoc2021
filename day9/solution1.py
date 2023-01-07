heightmap = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]
risk=0
for i in range(0,len(heightmap)):
    for j in range(0,len(heightmap[0])):
        if (i==0 or heightmap[i][j] < heightmap[i-1][j]) \
        and (i==len(heightmap)-1 or heightmap[i][j] < heightmap[i+1][j]) \
        and (j==0 or heightmap[i][j] < heightmap[i][j-1]) \
        and (j==len(heightmap[0])-1 or heightmap[i][j] < heightmap[i][j+1]):
           risk += heightmap[i][j] + 1       
print(risk)
