bin_str = ''.join([format(int(hx,16), '04b') for hx in open('input.txt', 'r').readline()])
pos=0
version_sum=0

def parse_packet():
    global pos, version_sum
    version_sum += int(bin_str[pos:pos+3],2)
    pack_type = int(bin_str[pos+3:pos+6],2)
    if pack_type==4:
        pos+=6
        while bin_str[pos]=='1':
            pos+=5
        pos+=5
        return
    if bin_str[pos+6]=='0':
        length_in_bits=int(bin_str[pos+7:pos+22],2)
        pos+=22        
        sub_startpos=pos
        while pos < sub_startpos+length_in_bits:
            parse_packet()
    else:
        packets=int(bin_str[pos+7:pos+18],2)
        pos+=18
        for i in range(packets):
            parse_packet()

parse_packet()
print(version_sum)