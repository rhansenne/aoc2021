depth=hor=0
with open('input.txt') as file:
    for line in file:
        movement = line.strip().split(' ')
        match movement[0]:
            case 'forward':
                hor += int(movement[1])
            case 'down':
                depth += int(movement[1])
            case 'up':
                depth -= int(movement[1])
print(depth*hor)