from sympy import Point, Segment
from itertools import combinations

lines = [Segment(p[0],p[1]) for p in [[Point([int(co) for co in point.split(',')]) for point in line.strip().split(' -> ')] for line in open('input.txt', 'r').readlines()]]
intersection_points=set()
for combo in combinations(lines, 2): #takes a while to complete on large data sets
    for int in combo[0].intersection(combo[1]):
        if isinstance(int, Segment):
            if int.slope == 0:
                for x in range(min(int.p1.x,int.p2.x),max(int.p1.x,int.p2.x)+1):
                    intersection_points.add(Point(x,int.p1.y))
            elif int.slope == float('inf'):
                for y in range(min(int.p1.y,int.p2.y),max(int.p1.y,int.p2.y)+1):
                    intersection_points.add(Point(int.p1.x,y))
            elif int.slope == 1:
                for i in range(max(int.p1.x,int.p2.x)-min(int.p1.x,int.p2.x)+1):
                    intersection_points.add(Point(min(int.p1.x,int.p2.x)+i,min(int.p1.y,int.p2.y)+i))
            elif int.slope == -1:
                for i in range(max(int.p1.x,int.p2.x)-min(int.p1.x,int.p2.x)+1):
                    intersection_points.add(Point(min(int.p1.x,int.p2.x)+i,max(int.p1.y,int.p2.y)-i))
        else:
            if int.x % 1 == 0: # only include discrete intersection points
                intersection_points.add(int)
print(len(intersection_points))