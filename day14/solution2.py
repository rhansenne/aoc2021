import re

input = open('input.txt', 'r').readlines()
polymer=input[0].strip()
rules = [rule.strip().split(' -> ') for rule in input[slice(2,len(input))]]
pair_freqs={}
element_freqs={}
elements=set(e[1] for e in rules)
for i in elements:
    element_freqs[i] = polymer.count(i)
    for j in elements:
        pair_freqs[i+j] = len(re.findall('(?='+(i+j)+')', polymer))
for step in range(0,40):
    freq_changes={}
    for i in elements:
        for j in elements:
            freq_changes[i+j]=0
    for rule in rules:
        freq_changes[rule[0]]-=pair_freqs[rule[0]]
        freq_changes[rule[0][0]+rule[1]]+=pair_freqs[rule[0]]
        freq_changes[rule[1]+rule[0][1]]+=pair_freqs[rule[0]]
        element_freqs[rule[1]]+=pair_freqs[rule[0]]
    for i in elements:
        for j in elements:
            pair_freqs[i+j]+=freq_changes[i+j]
print(max(element_freqs.values())-min(element_freqs.values()))
