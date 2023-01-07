signals = [[tuple(filter(None,[s for s in sig.split(' ')])) for sig in line.strip().split('|')] for line in open('input.txt', 'r').readlines()]
count=0
for signal in signals:
    for digit in signal[1]:
        if (len(digit) in (2,3,4,7)):
            count += 1
print(count)
