import re
players = [[int(d) for d in re.findall('(\d+)', line)] for line in open('input.txt', 'r').readlines()]
die=1
totalthrows=0
won=False
while True:
    for player in players:
        if len(player)==2:
            player[1]-=1 #0 based positioning
            player.append(0) #score
        rolls=0
        for throws in range(3):
            rolls+=die
            die+=1
            totalthrows+=1
            if die>100:
                die=1
        pos=(player[1]+rolls)%10
        player[1]=pos
        player[2]+=pos+1
        if player[2]>=1000:
            if player == players[0]:
                print(players[1][2]*totalthrows)
            else:
                print(players[0][2]*totalthrows)                
            won=True
    if won: break