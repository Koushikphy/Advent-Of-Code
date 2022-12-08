# with open('sample.txt') as f:
with open('input.txt') as f:
    allLines = f.read().strip().splitlines()


# not a very good solution for this one, 
# can the four direction option be merged in a single loop?

treeGrid = [[int(j) for j in i] for i in allLines]

nLen = len(treeGrid)


def checkIfVisible(m,n):
    

    topLine = [treeGrid[i][n] for i in range(m)]
    if all([elem<treeGrid[m][n] for elem in topLine]) : return True
    bottomLine = [treeGrid[i][n] for i in range(m+1,nLen)]
    if all([elem<treeGrid[m][n] for elem in bottomLine]) : return True
    lefttLine = [treeGrid[m][i] for i in range(n)]
    if all([elem<treeGrid[m][n] for elem in lefttLine]) : return True
    rightLine = [treeGrid[m][i] for i in range(n+1,nLen)]
    if all([elem<treeGrid[m][n] for elem in rightLine]) : return True
    return False

s=2*nLen + 2*(nLen-2)
for r in range(1,nLen-1):
    for c in range(1,nLen-1):
        if checkIfVisible(r,c):
            s+=1


print(s)



# part 2 
def scenicScore(m,n):
    totScore = 1
    # topView
    tmpScore = 0
    for i in range(m-1,-1,-1):
        tmpScore+=1
        if treeGrid[i][n]>=treeGrid[m][n]:
            break
    totScore *= tmpScore


    # bottom view
    tmpScore = 0
    for i in range(m+1,nLen):
        tmpScore+=1
        if treeGrid[i][n]>=treeGrid[m][n]:
            break
    totScore *= tmpScore


    # left view 
    tmpScore = 0
    for i in range(n-1,-1,-1):
        tmpScore+=1
        if treeGrid[m][i]>=treeGrid[m][n]:
            break
    totScore *= tmpScore


    # right view 
    tmpScore = 0
    for i in range(n+1,nLen):
        tmpScore+=1
        if treeGrid[m][i]>=treeGrid[m][n]:
            break
    totScore *= tmpScore


    return totScore



s = 0
for r in range(1,nLen-1):
    for c in range(1,nLen-1):
        ss = scenicScore(r,c)
        s = max(s,ss)
print(s)