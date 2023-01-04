timers = [0]*9 # amount of fish per timer
for t in [int(n) for n in open('input.txt', 'r').readline().split(',')]:
    timers[t] += 1
for day in range(0,256):
    spawning = timers[0]
    for i in range(0, len(timers)-1):
        timers[i] = timers [i+1]
    timers[6] += spawning
    timers[8] = spawning
print(sum(timers))
