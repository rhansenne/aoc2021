braces = { '(':')', '[':']', '{':'}', '<':'>'}
points = { '(':1, '[':2, '{':3, '<':4}
scores=[]
for line in open('input.txt', 'r').readlines():
    line = [*line.strip()] 
    stack = []
    corrupt = False
    for brace in line:
        if brace in braces.keys():
            stack.append(brace)
        else:
            if braces[stack.pop()] != brace:
                corrupt = True
    if corrupt:
        continue
    score=0
    while len(stack)>0:
        score = score * 5 + points[stack.pop()]
    scores.append(score)
scores.sort()    
print(scores[int(len(scores)/2)])