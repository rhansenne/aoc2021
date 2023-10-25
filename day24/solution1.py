instructions = [instruction.strip() for instruction in open('input.txt', 'r').readlines()]

def get(b, variables): 
    if b in variables:
        return variables[b]
    else:
        return int(b)

def next_instruction_block(start_line, frozen_variables, inp):
    variables=frozen_variables.copy()
    line=start_line
    for instruction in instructions[start_line:]:
        match instruction[:3]:
            case 'inp':
                if line!=start_line:
                    return (line,variables)
                variables[instruction[4]] = inp
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

def next_digit(start_line, variables, prev_inputs):
    if start_line < len(instructions):
        for inp in reversed(range(1,10)):
            prev_inputs_copy = prev_inputs.copy()
            prev_inputs_copy.append(inp)
            v=next_instruction_block(start_line, variables, inp)
            if v[1]['z']==0:
                print(''.join([str(d) for d in prev_inputs_copy]))
                exit()
            if not (((len(prev_inputs_copy)==6 or len(prev_inputs_copy)==7) and v[1]['x']!=0) or (len(prev_inputs_copy)==11 and v[1]['z']>200000) or (len(prev_inputs_copy)>=14)): #determined by manually analyzing the ALU program logic
                next_digit(v[0], v[1], prev_inputs_copy)

next_digit(0, {'w':0,'x':0,'y':0,'z':0}, [])