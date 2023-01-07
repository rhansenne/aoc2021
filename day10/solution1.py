braces = { '(':')', '[':']', '{':'}', '<':'>'}
points = { ')':3, ']':57, '}':1197, '>':25137}
total=0
for line in open('input.txt', 'r').readlines():
    line = [*line.strip()] 
    stack = []
    for brace in line:
        if brace in braces.keys():
            stack.append(brace)
        else:
            if braces[stack.pop()] != brace:
                total+=points[brace]
print(total)
