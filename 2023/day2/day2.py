from collections import defaultdict


# with open('./input.txt') as f:
with open('./sample.txt') as f:
    ttt = f.read().split('\n')


def isValid(line):
    b = line.strip().split(';')
    for bb in b:
        tt = defaultdict(lambda : 0 )
        for c in bb.strip().split(','):
            t1,t2 = c.split()
            tt[t2] = int(t1)
        if tt['red']>12 or tt['green']>13 or tt['blue']>14:
            return False
    return True

def getPower(line):
    b = line.strip().split(';')
    tt = defaultdict(lambda : 0 )
    for bb in b:
        for c in bb.strip().split(','):
            t1,t2 = c.split()
            tt[t2] = max([int(t1),tt[t2]])
    return tt['red']*tt['green']*tt['blue']



res = 0
res2 = 0

for t in ttt:
    a,b = t.split(':')

    if isValid(b): res+= int(a.strip('Game '))
    res2+=getPower(b)
print(res)
print(res2)
