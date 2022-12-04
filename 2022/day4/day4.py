import numpy as np 

# with open('sample.txt') as f:
with open('input.txt') as f:
    dat = f.read().strip().splitlines()

def getList(l):
    a,b = l.split('-')
    return list(range(int(a),int(b)+1))

part1, part2 = 0, 0

for i in dat:
    f,s = i.split(',')

    a1,a2 = getList(f), getList(s)
    aa = set([*a1,*a2])

    if (len(a1)==len(aa)) or (len(a2)==len(aa)): part1+=1
    if (len(a1)+len(a2)) != len(aa): part2+=1

print(part1,part2)