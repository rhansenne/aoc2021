gamma=epsilon=numbers=0
ones=[]
with open('input.txt') as file:
    for line in file:
        if len(ones) == 0:
            ones = ones=[0] * len(line.strip())
        for i, bit in enumerate([*line]):
            if bit == '1':
                ones[i] += 1
        numbers += 1
for x in range(0, len(ones)):
    if (ones[x] >= numbers / 2):
        gamma += pow(2,len(ones)-x-1)
    else:
        epsilon += pow(2,len(ones)-x-1)
print(gamma*epsilon)