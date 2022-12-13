# with open('./sample.txt') as f:
with open('./input.txt') as f:
    lines = f.read().strip().splitlines()
    values = [[ list(map(int,j.split(','))) for j in i.split(' -> ') ] for i in lines]




rocks = set()
minY = 0  # last possible floor
# making the rock grid  line
for val in values:
    for i in range(len(val)-1):
        (x1,y1),(x2,y2) = val[i], val[i+1]
        if x1==x2:
            for yi in range(min(y1,y2), max(y1,y2)+1):
                rocks.add((x1,yi))
                minY = max(minY,yi)
        elif y1==y2:
            for xi in range(min(x1,x2),max(x1,x2)+1):
                rocks.add((xi,y1))
            minY = max(minY,y1)






def getSandCount_part1():
    count = 0
    while True: # new sand
        sx,sy = 500,0
        while True: # sand falling through rocks
            if sy==minY:
                return count
            if (p:=(sx,sy+1)) not in rocks or (p:=(sx-1,sy+1)) not in rocks or (p:=(sx+1,sy+1)) not in rocks:
                sx,sy= p
            else:
                break
        # sand will get stuck now
        rocks.add((sx,sy))
        count +=1



def getSandCount_part2():
    count = 0
    while True: # new sand
        sx,sy = 500,0
        while True: # sand falling through rocks
            if sy==(minY+1): # can be one place further down
                break
            if (p:=(sx,sy+1)) not in rocks or (p:=(sx-1,sy+1)) not in rocks or (p:=(sx+1,sy+1)) not in rocks:
                sx,sy= p
            else:
                break
        # sand will get stuck now
        rocks.add((sx,sy))
        count +=1
        if sx==500 and sy==0: # sand stuck at the entrance
            break
    return count

abyss = minY
print(getSandCount_part2())
# print(getSandCount_part1())
