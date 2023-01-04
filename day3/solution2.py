def onesAtPosition(lines, pos):
    count=0
    for line in lines:
        if line[pos] == '1': count += 1
    return count

def filterList(lines, keepIfMostFreq):
    for i in range(0, len(lines[0])):
        if onesAtPosition(lines,i) >= len(lines) / 2 and len(lines) > 1:
            lines = [x for x in lines if x[i]==keepIfMostFreq]
        elif len(lines) > 1:
            lines = [x for x in lines if x[i]!=keepIfMostFreq]
    return lines[0]
    
with open('input.txt') as file:
    lines = [line.strip() for line in file]
print(int(filterList(lines,'1'),2) * int(filterList(lines,'0'),2))