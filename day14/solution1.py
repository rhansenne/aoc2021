import re

input = open('input.txt', 'r').readlines()
polymer=input[0].strip()
for step in range(0,10):
    inserts_per_index={}
    for rule in input[slice(2,len(input))]:
        between = rule.split(' -> ')[0]
        pos = [m.start()+1 for m in re.finditer('(?='+between+')', polymer)] 
        for p in pos:
            inserts_per_index[p]= rule.split(' -> ')[1].strip() 
    indices=list(inserts_per_index.keys())
    indices.sort()
    inserts=0
    for i in indices:
        polymer = polymer[:i+inserts] + inserts_per_index[i] + polymer[i+inserts:]
        inserts+=1
occurrences = [polymer.count(element) for element in set(polymer)]
print(max(occurrences)-min(occurrences))