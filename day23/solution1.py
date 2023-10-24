import copy

to_int={'A':0,'B':1,'C':2,'D':3}
diagram=[[-1 for col in range(11)] ]
for lnr, line in enumerate(open('input.txt', 'r').readlines()):
    if 1<lnr<4:
        diagram.append([to_int[line[3]],to_int[line[5]],to_int[line[7]],to_int[line[9]]])

min_energy=float('inf')

def completed(diag):
    if diag[1]==diag[2]==[0,1,2,3]:
        return True;
    return False

def amphipods_in_hallway(diag):
    return sum([1 for i in diag[0] if i>=0])

def diag_to_tuple(diag):
    return (tuple(diag[0]),tuple(diag[1]),tuple(diag[2]))

def move_to_hallway(diag,row,col):
    energy_per_step=pow(10,diag[row][col])
    destcol_energy=[]
    energy_to_hallway=0
    if row==2 and col==diag[row][col]: #already in room
        return destcol_energy
    if row==1 and col==diag[row][col]==diag[2][col]: #already in room and below also already in room
        return destcol_energy

    if row==2 and diag[1][col]==-1:
        row=0
        col=col*2+2
        energy_to_hallway+=2*energy_per_step
    if row==1: 
        row=0
        col=col*2+2
        energy_to_hallway+=energy_per_step
    if row==0:
        for i in (0,1,3,5,7,9,10):
            if diag[0][i]==-1:
                free_path=True
                for j in range(min(i,col)+1,max(i,col)):
                    if diag[0][j]>=0:
                        free_path=False
                if free_path:
                    destcol_energy.append((i, energy_to_hallway + (max(i,col)-min(i,col))*energy_per_step))
    return tuple(destcol_energy)            

def move_to_room(diag,row,col):
    energy_to_room=0
    row1_col=diag[row][col]
    col_above_room=row1_col*2+2
    if diag[1][row1_col]>=0: #room occupied
        return None
    if diag[2][row1_col]>=0 and diag[2][row1_col]!=row1_col: #room bottom occupied by other type
        return None
    energy_per_step=pow(10,diag[row][col])
    if row==2:
        if diag[1][col]>=0:
            return None
        row=0
        col=col*2+2
        energy_to_room=2*energy_per_step
    if row==1:
        row=0
        col=col*2+2
        energy_to_room=energy_per_step
    for j in range(min(col_above_room,col)+1,max(col_above_room,col)):
        if diag[0][j]>=0:
            return None
    energy_to_room+= (max(col_above_room,col)-min(col_above_room,col))*energy_per_step
    if diag[2][row1_col]==-1:
        energy_to_room+=2*energy_per_step
        return (2,energy_to_room)
    else:
        energy_to_room+=energy_per_step
        return (1,energy_to_room)

def next_move(diag,energy,last_moved):
    global min_energy
    if energy>=min_energy:
        return
    if completed(diag):
        if energy<min_energy:
            min_energy=energy
        return  
    diag_tuple = diag_to_tuple(diag)
    for i,row in enumerate(diag):
        for j,anthropod in enumerate(row):
            if anthropod>=0 and not last_moved==(i,j) and not (i==2 and j==anthropod) and not (i==1 and j==anthropod==diag[2][j]): #don't move if already in place
                in_hallway=amphipods_in_hallway(diag)
                if in_hallway>0:                   
                    destrow_energy = move_to_room(diag_tuple, i, j)
                    if destrow_energy is not None and (energy+destrow_energy[1])<min_energy:
                        diag_copy = copy.deepcopy(diag)
                        diag_copy[i][j]=-1
                        diag_copy[destrow_energy[0]][anthropod]=anthropod
                        next_move(diag_copy,energy+destrow_energy[1],(destrow_energy[0],anthropod))                            
                if i>0 and in_hallway<3: # don't allow more than 3 amphipods in the hallway                    
                    destcol_energy = move_to_hallway(diag_tuple, i, j)
                    for move in destcol_energy:
                        diag_copy = copy.deepcopy(diag)
                        diag_copy[i][j]=-1
                        diag_copy[0][move[0]]=anthropod
                        if (energy+move[1])<min_energy:
                            next_move(diag_copy,energy+move[1],(0,move[0]))
                 
next_move(diagram,0,(0,0))
print(min_energy)