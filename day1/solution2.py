counter=0; prevsum=prev1=prev2=-1
with open('input.txt') as file:
    for line in file:
        current = int(line)
        if prev2 > 0:
            currentsum = current + prev1 + prev2
            if currentsum > prevsum > 0:
                counter += 1
            prevsum = currentsum
        prev2 = prev1
        prev1 = current
print(counter)