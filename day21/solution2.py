import re

class Player:
    def __init__(self, num, pos, score):
        self.num=num
        self.pos=pos
        self.score=score

players = [[int(d) for d in re.findall('(\d+)', line)] for line in open('input.txt', 'r').readlines()]
p1_wins=p2_wins=0
roll_chance={}
for i in (1,2,3):
    for j in (1,2,3):
        for k in (1,2,3):
            sum=i+j+k
            if sum in roll_chance:
                roll_chance[sum]+=1
            else:
                roll_chance[sum]=1   

def all_possible_rolls(active_player,waiting_player,universes):
    global p1_wins,p2_wins
    for roll in roll_chance.items():
        ap_copy=Player(active_player.num,active_player.pos,active_player.score)
        ap_copy.pos=(ap_copy.pos+roll[0])%10
        ap_copy.score+=ap_copy.pos+1
        if ap_copy.score >= 21:
            if ap_copy.num==1:
                p1_wins+=universes*roll[1]
            else:
                p2_wins+=universes*roll[1]
        else:
            all_possible_rolls(waiting_player,ap_copy,universes*roll[1])

p1=Player(players[0][0],players[0][1]-1,0)
p2=Player(players[1][0],players[1][1]-1,0)
all_possible_rolls(p1,p2,1)
print(max(p1_wins,p2_wins))