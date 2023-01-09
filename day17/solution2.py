import re

target = [int(pos) for pos in re.findall('(-?[0-9]+)', open('input.txt', 'r').readline())]
hit=set()
for x_vel in range(1,target[1]+1):
    for y_vel in range(target[2],-target[2]+1):
        x=y=0
        for step in range(target[1]):
            x+=max(0,x_vel-step)
            y+=y_vel-step
            if target[0]<=x<=target[1] and target[2]<=y<=target[3]:
                hit.add((x_vel,y_vel))
                continue
            if x>target[1] or y<target[2]:
                continue
print(len(hit))