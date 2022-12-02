import numpy as np 

# with open('sample.txt') as f:
with open('input.txt') as f:
    dat = f.read().strip().split('\n')
    dat = [i.split() for i in dat]


# part 1----------------------------------------------------------------------------
# Rock > Scissors, Scissors > Paper, and Paper > Rock


dic ={
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    "X": 1,
    "Y": 2,
    "Z": 3
}


score = 0

for i,j in dat:
    he = dic[i] 
    me = dic[j]

    score +=me

    if he==me: # draw 
        score +=3
    
    elif (he==3 and me==1) or (he==1 and me ==2) or (he==2 and me==3):# win 
        score +=6 

print(score)


# part 2----------------------------------------------------------------------------


score = 0 

for i,j in dat:
    he = dic[i] 
    me = dic[j]

    if j=='Y': # draw
        score +=he + 3

    elif j=='X' : #lose
        the = he-1
        if the ==0:
            the = 3
        score += the + 0 

    elif j=='Z': # win
        the = he+1
        if the==4:
            the= 1
        score += the + 6


print(score)