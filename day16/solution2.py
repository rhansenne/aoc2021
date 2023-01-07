from functools import reduce

bin_str = ''.join([format(int(hx,16), '04b') for hx in open('input.txt', 'r').readline()])
pos=0

def parse_packet():
    global pos, version_sum
    pack_type = int(bin_str[pos+3:pos+6],2)
    if pack_type==4:
        pos+=6
        lit=''
        while bin_str[pos]=='1':
            lit+=bin_str[pos+1:pos+5]
            pos+=5
        lit+=bin_str[pos+1:pos+5]
        pos+=5
        return int(lit,2)
    subs=[]
    if bin_str[pos+6]=='0':
        length_in_bits=int(bin_str[pos+7:pos+22],2)
        pos+=22        
        sub_startpos=pos
        while pos < sub_startpos+length_in_bits:
            subs.append(parse_packet())
    else:
        packets=int(bin_str[pos+7:pos+18],2)
        pos+=18
        for i in range(packets):
            subs.append(parse_packet())
    match pack_type:
        case 0:
            return sum(subs)
        case 1:
            return reduce((lambda x, y: x * y), subs)
        case 2:
            return min(subs)
        case 3:
            return max(subs)
        case 5:
            return 1 if subs[0]>subs[1] else 0
        case 6:
            return 1 if subs[0]<subs[1] else 0
        case 7:
            return 1 if subs[0]==subs[1] else 0

print(parse_packet())