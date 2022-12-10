# with open('sample.txt') as f:
# # with open('input.txt') as f:
#     allLines = f.read().strip().splitlines()


# n = len(allLines)



# signalArray = [0 for _ in range(n)]
# cycleArray = [1 for _ in range(n)]


# for i,elem in enumerate(allLines):
#     words = elem.split()
#     if words[0] == "addx":
#         signalArray[i] = int(words[1])
#         cycleArray[i] = 2



# for i in range(1,n):
#     cycleArray[i]+= cycleArray[i-1]
#     signalArray[i]+=signalArray[i-1]


# sIn = 0
# totSigStrength = 0 
# while True:
#     index = 20+sIn*40  # where to look for signal
#     found = False
#     for i,cycle in enumerate(cycleArray):
#         if (cycle-index)>=0: # cycle just crossed the index
#             signalStrength = index*(1+signalArray[i-1])
#             totSigStrength +=signalStrength
#             found = True
#             break

#     if not found: break
#     sIn +=1

# print(totSigStrength)




# with open('sample.txt') as f:
with open('input.txt') as f:
    allLines = f.read().strip().splitlines()



screen = [["." for _ in range(40)] for _ in range(6)]


def checkSpriteCRT(cycle,x):
    index =cycle-1
    row = index//40
    col = index%40
    pix = "."
    if (col-1)<=x<=(col+1): 
        pix = "#"
    return row,col,pix


cyCleToCheck =[20,60,100,140,180,220]

cycle = 0 
X = 1
sngStrength = 0


for elem in allLines:
    elems = elem.split()
    if elems[0]=="noop":
        # these are repeatative !!?
        cycle +=1
        r,c,p = checkSpriteCRT(cycle,X)
        screen[r][c] = p
        if cycle in cyCleToCheck:
            sngStrength += cycle*X

    if elems[0]=='addx':

        cycle += 1
        r,c,p = checkSpriteCRT(cycle,X)
        screen[r][c] = p
        if cycle in cyCleToCheck:
            sngStrength += cycle*X

        cycle += 1
        r,c,p = checkSpriteCRT(cycle,X)
        screen[r][c] = p
        if cycle in cyCleToCheck:
            sngStrength += cycle*X

        X += int(elems[1])

print(sngStrength)



for row in screen:
    print(''.join(row))