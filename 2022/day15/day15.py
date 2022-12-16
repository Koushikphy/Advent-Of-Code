import re 

rx = re.compile(r'(-?\d+)')


coord = []

sY = 10
high = 20
# with open('./sample.txt') as f:
sY=2000000
high=4000000
with open('./input.txt') as f:
    lines = f.read().strip().splitlines()
    coord = [list(map(int,rx.findall(i))) for i in lines]







noB = set()

for x1,y1,x2,y2 in coord:
    if (disOffX:=(abs(x1-x2)+abs(y1-y2) - abs(y1-sY)))<0:
    # absolute distance, so range of x is just the total distance - the perpendicular distance
        continue

    for xi in range(x1-disOffX,x1+disOffX+1):
        noB.add(xi)

for _,_,x2,y2 in coord:
    if y2==sY and x2 in noB:
        noB.remove(x2)

print(len(noB))



# part 2 ------

for hgY in range(high+1):
    ranges = []

    for x1,y1,x2,y2 in coord:

        if (disOffX:=(abs(x1-x2)+abs(y1-y2) - abs(y1-hgY)))<0:
        # absolute distance, so range of x is just the total distance - the perpendicular distance
            continue

        ranges.append((x1-disOffX,x1+disOffX))

    ranges.sort()

    lower=0
    upper=ranges[0][0]
    for i in range(len(ranges)-1):
        # find if a gap inbetween the ranges exist
        # the beacon should be in the gap
        lower= max(lower,ranges[i][1])
        upper=max(upper,ranges[i+1][0])
        if lower<upper:
            # also there should be a single gap in between the ranges 
            assert lower+2==upper
            print(hgY,lower,upper,(lower+1)*high+hgY)  # 3349056 3418491 3418493
            exit(0)



