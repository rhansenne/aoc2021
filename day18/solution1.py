import re, math
    
def split(number):
    result=[]
    split=False
    for i in number:
        if type(i) == int and i>=10 and not split:
            result.extend([ '[' , math.floor(i/2) , math.ceil(i/2) , ']']) 
            split=True  
        else:
            result.append(i)
    return (split,result)

def explode(number):
    result=[]
    i=nesting=0
    exploded=False
    while i < len(number):
        match number[i]:
            case '[':
                nesting+=1
                result.append('[')
            case ']':
                nesting-=1
                result.append(']')
            case _:
                if nesting>=5 and type(number[i+1])==int and not exploded:
                    result.pop();
                    for left in reversed(range(0,len(result))):
                        if type(result[left]) == int:
                            result[left]+=number[i]
                            break
                    for right in range(i+3,len(number)):
                        if type(number[right]) == int:
                            number[right]+=number[i+1]
                            break
                    exploded=True
                    result.append(0)
                    i+=2
                else:
                    result.append(number[i])
        i+=1
    return (exploded,result)

def mag(number):
    while len(number)>1:
        tmp=[]
        i=0
        while i < len(number):
            match number[i]:
                case '[':
                    if number[i+3] == ']':
                        tmp.append(3*number[i+1]+2*number[i+2])
                        i+=3
                    else:                    
                        tmp.append(number[i])
                case _:
                    tmp.append(number[i])
            i+=1
        number=tmp
    return number[0]

sum=None
numbers = [re.findall('(?:\[|\]|\d+)', line) for line in open('input.txt', 'r').readlines()]
for number in numbers:
    for i, e in enumerate(number):
        if e.isnumeric():
            number[i]=int(e)
    if sum == None:
        sum = number
        continue
    else:
        sum.insert(0,'[')
        sum.extend(number)
        sum.append(']')
        while True:
            expl = explode(sum)
            if expl[0]:
                sum=expl[1]
                continue
            splt = split(sum)
            if splt[0]:
                sum=splt[1]
                continue
            break
print(mag(sum))