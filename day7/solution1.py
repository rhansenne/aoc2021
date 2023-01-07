positions = [int(n) for n in open('input.txt', 'r').readline().split(',')]
min_fuel = float('inf')
for pos in range(min(positions), max(positions)+1):
    min_fuel = min(min_fuel, sum([abs(pos-x) for x in positions]))
print(min_fuel)
        
