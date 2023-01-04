timers = [int(n) for n in open('input.txt', 'r').readline().split(',')]
for day in range(0,80):
    for i, t in enumerate(timers):
        if timers[i] == 0:
            timers[i] = 7
            timers.append(9)
        timers[i] -= 1    
print(len(timers))
        
