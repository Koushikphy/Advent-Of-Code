import re



with open('./sample.txt') as f:
    txt = f.read().splitlines()
    grid = txt[:-2]
    print(txt[-1])
    instructions = re.findall(r'\d+|[RL]',txt[-1])

row,col = 0,0
for i,c in enumerate(grid[0]):
    if c=='.':
        col=i
        break


dx,dy = 1,0 # right
for ins in instructions:
    if ins.isdigit():
        for _ in range(int(ins)):
            hx = len(grid[row])
            hy = len(grid)
            tmpRow, tmpCol = row, col
            while True:
                tmpRow += dy 
                tmpRow %= hy
                tmpCol += dx
                tmpCol %= hx
                if grid[tmpRow][tmpCol] != ' ':
                    row = tmpRow
                    col = tmpCol
                    break
            if grid[row][col] == '#' :
                break

            row += dy
            col += dx   
    elif ins=="R":
        dx,dy = dy, -dx
    elif ins=='L':
        dx,dy = -dy, dx
    else:
        print('W!')



print(row,col)