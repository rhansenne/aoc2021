instructions = [instruction.strip() for instruction in open('input.txt', 'r').readlines()]

def get(b, variables): 
    if b in variables:
        return variables[b]
    else:
        return int(b)

def next_instruction_block(start_line, frozen_variables, input):
    variables=dict(frozen_variables)
    line=start_line
    for instruction in instructions[start_line:]:
        match instruction[:3]:
            case 'inp':
                if line!=start_line:
                    return (line,variables)
                variables[instruction[4]] = input
            case 'add':
                variables[instruction[4]] = variables[instruction[4]] + get(instruction[6:],variables)
            case 'mul':
                variables[instruction[4]] = variables[instruction[4]] * get(instruction[6:],variables)
            case 'div':
                variables[instruction[4]] = variables[instruction[4]] // get(instruction[6:],variables)
            case 'mod':
                variables[instruction[4]] = variables[instruction[4]] % get(instruction[6:],variables)
            case 'eql':
                variables[instruction[4]] = 1 if variables[instruction[4]] == get(instruction[6:],variables) else 0
        line+=1
    return (line,variables)
            
for inp in range(1,10): #very quick and dirty - should refactor as recursive function
    variables={'w':0,'x':0,'y':0,'z':0}
    v=next_instruction_block(0, variables, inp)
    for inp2 in range(1,10):
        v2=next_instruction_block(v[0], v[1], inp2)
        for inp3 in range(1,10):
            v3=next_instruction_block(v2[0], v2[1], inp3)
            for inp4 in range(1,10):
                v4=next_instruction_block(v3[0], v3[1], inp4)
                for inp5 in range(1,10):
                    v5=next_instruction_block(v4[0], v4[1], inp5)
                    for inp6 in range(1,10):
                        v6=next_instruction_block(v5[0], v5[1], inp6)
                        if v6[1]['x']==0: #determined by manually analyzing the ALU program logic
                            for inp7 in range(1,10):
                                v7=next_instruction_block(v6[0], v6[1], inp7)
                                if v7[1]['x']==0: #determined by manually analyzing the ALU program logic
                                    for inp8 in range(1,10):
                                        v8=next_instruction_block(v7[0], v7[1], inp8)
                                        for inp9 in range(1,10):
                                            v9=next_instruction_block(v8[0], v8[1], inp9)
                                            for inp10 in range(1,10):
                                                v10=next_instruction_block(v9[0], v9[1], inp10)
                                                for inp11 in range(1,10):
                                                    v11=next_instruction_block(v10[0], v10[1], inp11)
                                                    if v11[1]['z']<200000: #cutoff determined through trial and error
                                                        for inp12 in range(1,10):
                                                            v12=next_instruction_block(v11[0], v11[1], inp12)
                                                            for inp13 in range(1,10):
                                                                v13=next_instruction_block(v12[0], v12[1], inp13)
                                                                for inp14 in range(1,10):
                                                                    v14=next_instruction_block(v13[0], v13[1], inp14)
                                                                    if v14[1]['z']==0:
                                                                        print(inp,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14)
                                                                        exit()
