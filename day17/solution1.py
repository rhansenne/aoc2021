import re

target = [int(pos) for pos in re.findall('(-?[0-9]+)', open('input.txt', 'r').readline())]
max_height=0
for x_vel in range(1,target[1]+1):
    for y_vel in range(1,abs(target[2])+1):
        x=y=y_max=0
        for step in range(target[1]):
            x+=max(0,x_vel-step)
            y+=y_vel-step
            if y>y_max:
                y_max=y
            if target[0]<=x<=target[1] and target[2]<=y<=target[3]:
                if y_max>max_height:
                    max_height=y_max
                continue
            if x>target[1] or y<target[2]:
                continue
print(max_height)