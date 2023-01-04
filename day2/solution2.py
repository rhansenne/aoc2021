depth=hor=aim=0
with open('input.txt') as file:
    for line in file:
        movement = line.strip().split(' ')
        match movement[0]:
            case 'forward':
                hor += int(movement[1])
                depth += aim * int(movement[1])
            case 'down':
                aim += int(movement[1])
            case 'up':
                aim -= int(movement[1])
print(depth*hor)