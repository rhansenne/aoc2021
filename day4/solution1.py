lines = open('input.txt', 'r').readlines()
draws = [int(num) for num in lines[0].strip().split(',')]
boards = [[[int(num) for num in filter(None, line.strip().split(' '))] for line in lines[slice(2+i*6, 7+i*6)]] for i in range(0,int(len(lines)/6))]

def isWin(board,numbers):
    for row in board:
        if sum(number for number in row if number not in numbers)==0:
            return True
    for col in zip(*board):
        if sum(number for number in col if number not in numbers)==0:
            return True
    return False

for numbersDrawn in range(1,len(draws)):
    for board in boards:
        if isWin(board,draws[slice(0,numbersDrawn)]):
            print(draws[numbersDrawn-1] * sum(sum(number for number in row if number not in draws[slice(0,numbersDrawn)]) for row in board))
            exit()