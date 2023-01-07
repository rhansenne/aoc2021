signals = [[tuple(filter(None,[s for s in sig.split(' ')])) for sig in line.strip().split('|')] for line in open('input.txt', 'r').readlines()]
numbers = { 
        0 : {'a','b','c','e','f','g'},
        1 : {'c','f'},
        2 : {'a','c','d','e','g'},
        3 : {'a','c','d','f','g'},
        4 : {'b','c','d','f'},
        5 : {'a','b','d','f','g'},
        6 : {'a','b','d','e','f','g'},
        7 : {'a','c','f'},
        8 : {'a','b','c','d','e','f','g'},
        9 : {'a','b','c','d','f','g'}
    }
numbers_by_nr_of_segments = { len(numbers[key]):set(num for num in numbers.keys() if len(numbers[num])==len(numbers[key])) for key in numbers.keys() }

def certainly_included(segments):
    included = set()
    for segment in segments:
        if len(mapping[segment]) == 1:
            included.update(mapping[segment])
        elif len(mapping[segment]) == 2:
            for other_segment in segments:
                if other_segment != segment and mapping[segment] == mapping[other_segment]:
                    included.update(mapping[segment]) 
    return included

def update_mapping(mapping, segments, options):
    for segment in segments:
        mapping[segment] = mapping[segment].intersection(options)
    all_segments = set(s for s in mapping.keys())
    for segment in all_segments:
        other_segments = all_segments.copy()
        other_segments.remove(segment)
        mapping[segment] -= certainly_included(other_segments)

def decode(digit, mapping):
    mapped = set()
    for segment in digit:
        mapped.update(mapping[segment])
    return [number for number, segs in numbers.items() if segs == mapped][0]
        
sum=0
for signal in signals:
    mapping = {}   
    for l in range(ord('a'),ord('g')+1):
        mapping[chr(l)]=set(chr(c) for c in  range(ord('a'),ord('g')+1))
    for digit in sorted(signal[0], key=len):
        segments = set(c for c in digit)
        options = set()
        for number in numbers_by_nr_of_segments[len(digit)]:
             if certainly_included(segments).issubset(numbers[number]):
                  options.update(numbers[number])
        update_mapping(mapping,segments,options)
    for i, digit in enumerate(signal[1]):
        sum += decode(digit, mapping) * pow(10,3-i)
print(sum)