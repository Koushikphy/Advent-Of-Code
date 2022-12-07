with open('sample.txt') as f:
# with open('input.txt') as f:
    allLines = f.read().strip().splitlines()


fileSys = {}
currentPath = []

for line in allLines:
    ins = line.strip().split()
    if ins[0]=='$': # a command
        if ins[1] == 'cd':
            if ins[2]=='..': # cd back
                currentPath.pop()
            else:  # cd to
                currentPath.append(ins[2])

    # must be out put of ls
    elif ins[0]=='dir': # just ignore directories
        continue

    else: # must be files 
        value = int(ins[0])
        for i in range(1,len(currentPath)+1):
            # value need to be added to it and all its parent
            fullPath = '/'.join(currentPath[:i])
            if fullPath in fileSys:
                fileSys[fullPath] += value
            else:
                fileSys[fullPath] = value


# part 1 -------------
p1 = 0
for k,v in fileSys.items():
    if v<100000:
        p1+=v
print(p1)


# part 2 ------------
canBeUsed = 70000000-30000000
remove = fileSys['/'] - canBeUsed

p2 = 70000000
for k,v in fileSys.items():
    if v>remove:
        p2 = min(p2,v)
print(p2)
