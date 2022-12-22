from collections import Counter

with open('./input.txt') as f:
# with open('./sample.txt') as f:
    lines = f.read().strip().split('\n')
    data = [list(map(int,i.split(','))) for i in lines]




sides = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
sides = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]
faces = []
for d1,d2,d3 in data:
    for x,y,z in sides:
        faces.append((d1+x,d2+y,d3+z))


tot = 0
for i in Counter(faces).values():
    if i==1:
        tot +=1

print(tot)

