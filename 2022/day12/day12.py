from collections import deque


# with open('./input.txt') as f:
with open('./input.txt') as f:
    lines = f.read().strip().splitlines()
    grid = [list(i) for i in lines]

m,n = len(grid), len(grid[0])
start, end = (0,0), (0,0)

for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col=='S':
            start = (r,c)
            grid[r][c] = ord('a')
        elif col=='E':
            end = (r,c)
            grid[r][c] = ord('z')
        else:
            grid[r][c] = ord(col)


#BFS algorithm
directions = [[1,0],[-1,0],[0,1],[0,-1]]

visited = [[False for _ in range(n)] for _ in range(m)]

myQueue = deque()
myQueue.append((0,*start))
visited[start[0]][start[1]] = True


while len(myQueue)>0:
    dis, cRow, cCol = myQueue.popleft()

    if cRow==end[0] and cCol==end[1]: # target reached
        print(dis)
        break
    
    for (dt,dr) in directions:
        nRow,nCol = cRow+dt, cCol+dr

        if (0<=nRow<m) and (0<=nCol<n) and (not visited[nRow][nCol]) and (grid[nRow][nCol]-grid[cRow][cCol])<=1:
            myQueue.append((dis+1,nRow,nCol))
            visited[nRow][nCol] = True



# part 2 is just the opposite, start from the highest point and end on the lowest, with shortest route

visited = [[False for _ in range(n)] for _ in range(m)]

myQueue = deque()
myQueue.append((0,*end))
visited[end[0]][end[1]] = True



while len(myQueue)>0:
    dis, cRow, cCol = myQueue.popleft()

    if grid[cRow][cCol]==ord('a'): # target reached
        print(dis)
        break
    
    for (dt,dr) in directions:
        nRow,nCol = cRow+dt, cCol+dr

        if (0<=nRow<m) and (0<=nCol<n) and (not visited[nRow][nCol]) and (grid[cRow][cCol]-grid[nRow][nCol])<=1:
            myQueue.append((dis+1,nRow,nCol))
            visited[nRow][nCol] = True

