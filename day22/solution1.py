import re

def intersect(c1,c2):
    x1=max(c1[0],c2[0])
    x2=min(c1[1],c2[1])
    y1=max(c1[2],c2[2])
    y2=min(c1[3],c2[3])
    z1=max(c1[4],c2[4])
    z2=min(c1[5],c2[5])
    if x1>x2 or y1>y2 or z1>z2:
        return None
    return (x1,x2,y1,y2,z1,z2)

def vol(c):
    return (c[1]-c[0]+1)*(c[3]-c[2]+1)*(c[5]-c[4]+1)

on = [True if 'on' in line else False for line in open('input.txt', 'r').readlines()]
cuboids = [[int(d) for d in re.findall('(-?\d+)', line)] for line in open('input.txt', 'r').readlines()]
result=[]
for c in range(len(cuboids)):
    cuboids[c]=intersect(cuboids[c],[-50,51,-50,51,-50,51])
    if cuboids[c]==None:
        continue
    for lst in result:
        added=[]
        for cuboid in lst:
            intersection = intersect(cuboid[0],cuboids[c])
            if intersection is not None:
                if cuboid[1]:
                    added.append((intersection,False))
                else:
                    added.append((intersection,True))
        lst.extend(added)
    if on[c]:
        result.append([(cuboids[c],on[c])])
volume=0
for lst in result:
    for cuboid in lst:
        if cuboid[1]:
            volume+=vol(cuboid[0])
        else:
            volume-=vol(cuboid[0])
print(volume)