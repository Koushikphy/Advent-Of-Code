
direction = {
    "R": [1,0],
    "L": [-1,0],
    "U": [0,1],
    "D": [0,-1],
}

# direction as x,y coordinate
def findposition(hh,tt):
    dx = abs(hh[0] - tt[0])
    dy = abs(hh[1] - tt[1])
    
    # linear movement
    if dx==0 and dy==2:
        tt[1] += +1 if hh[1]>tt[1] else -1
    elif dy==0 and dx==2:
        tt[0] += +1 if hh[0]>tt[0] else -1
    
    # diagonal movement
    elif (dx==1 and dy==2) or (dy==1 and dx==2) or (dx==2 and dy==2):
        tt[0] += +1 if hh[0]>tt[0] else -1
        tt[1] += +1 if hh[1]>tt[1] else -1
    
    return tt



# part 1

with open('sample.txt') as f:
# with open('input.txt') as f:
    inst = f.read().strip().splitlines()
    inst = [i.split() for i in inst ]



head, tail, tailPos = [0,0], [0,0], set([(0,0)])


for to,step in inst:
    dtx,dty = direction[to]
    for kk in range(int(step)):
        
        head[0] += dtx
        head[1] += dty

        tail = findposition(head,tail)
        tailPos.add(tuple(tail))

print(len(tailPos))








# part 2

with open('sample2.txt') as f:
# with open('input.txt') as f:
    inst = f.read().strip().splitlines()
    inst = [i.split() for i in inst ]


head, tail, tailPos = [0,0], [[0,0] for _ in range(9)], set([(0,0)])
# this part can also be merged with the previous one
# counting tail[0] is exactly the same as previous one


for to,step in inst:
    dtx,dty = direction[to]
    for kk in range(int(step)):
        
        head[0] += dtx
        head[1] += dty

        tail[0] = findposition(head,tail[0])

        for i in range(1,9):
            tail[i] = findposition(tail[i-1],tail[i])


        tailPos.add(tuple(tail[-1]))

print(len(tailPos))

