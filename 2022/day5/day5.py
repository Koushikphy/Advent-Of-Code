import re

stacks_end = 3
with open('sample.txt') as f:
# # for input 
# stacks_end = 8
# with open('input.txt') as f:
    dat = f.read().splitlines()


# create the stacks from input
rs = re.compile(r'(?: ?)\[(\w)\]|(?:   )(?: ?)')
#^ match the letter or three spaces for blank, with 1 space padding
def getStacks(ll): 
    matches = [rs.findall(i) for i in ll]
    stacks =[]
    for i in zip(*matches):
        k = reversed(list(i))
        stacks.append([tt for tt in k if tt])
    return stacks



rx = re.compile(r'(\d+)')


stacks = getStacks(dat[:stacks_end])


# part 1 
for d in dat[stacks_end+2:]:
    n,i,j = rx.findall(d)
    n = int(n)
    i = int(i)-1
    j = int(j)-1
    for _ in range(n):
        stacks[j].append(stacks[i].pop())



print(''.join([i[-1] for i in stacks]))


# part 2
stacks = getStacks(dat[:stacks_end])

for d in dat[stacks_end+2:]:

    n,i,j = rx.findall(d)
    n = int(n)
    i = int(i)-1
    j = int(j)-1
    if n==1:
        stacks[j].append(stacks[i].pop())
    else:
        tmp = stacks[i][-n:]
        del stacks[i][-n:]
        stacks[j].extend(tmp)



print(''.join([i[-1] for i in stacks]))

