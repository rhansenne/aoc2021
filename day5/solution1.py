from sympy import Point, Segment
from itertools import combinations

lines = [Segment(p[0],p[1]) for p in [[Point([int(co) for co in point.split(',')]) for point in line.strip().split(' -> ')] for line in open('input.txt', 'r').readlines()]]
straight_lines = [s for s in lines if s.slope in [0, float('inf')]]
intersection_points=set()
for combo in combinations(straight_lines, 2): #takes a while to complete on large data sets
    for int in combo[0].intersection(combo[1]):
        if isinstance(int, Segment):
            if int.slope == 0:
                for x in range(min(int.p1.x,int.p2.x),max(int.p1.x,int.p2.x)+1):
                    intersection_points.add(Point(x,int.p1.y))
            else:
                for y in range(min(int.p1.y,int.p2.y),max(int.p1.y,int.p2.y)+1):
                    intersection_points.add(Point(int.p1.x,y))
        else:
            intersection_points.add(int)
print(len(intersection_points))