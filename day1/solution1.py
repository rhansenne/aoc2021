counter=0; prev=-1
with open('input.txt') as file:
    for line in file:
        if int(line) > prev > 0:
            counter += 1
        prev = int(line)
print(counter)