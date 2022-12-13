

with open('./input.txt') as f:
# with open('./sample.txt') as f:
    lines = f.read().strip().split('\n\n')





def checkOrder(left,right):
    lType, rType = type(left), type(right)

    if lType==int and rType==int:
        return None if left==right else left<right

    elif lType==list and rType==int:
        return checkOrder(left,[right])

    elif lType==int and rType==list:
        return checkOrder([left],right)

    else: # both is list
        for l,r in zip(left,right):
            if (v:=checkOrder(l,r)) is not None:
                return v
        return checkOrder(len(left), len(right))


grid = [list(map(eval,l.split('\n'))) for l in lines]

sum = 0
for ind,(a,b) in enumerate(grid,start=1):
    if checkOrder(a,b):
        sum += ind
print(sum)




div1, div2 = [[2]], [[6]]
d1, d2 = 1, 1

flattenGrid = [i for j in grid for i in j] + [ div1,div2 ]

for i,g in enumerate(flattenGrid):

    if checkOrder(g,div1): d1+=1
    if checkOrder(g,div2): d2+=1


print(d1,d2,d1*d2)