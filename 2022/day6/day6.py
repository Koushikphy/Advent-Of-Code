import numpy as np 

# with open('sample.txt') as f:
with open('input.txt') as f:
    dat = f.read().strip().splitlines()




def checkMarker(txt):
    return len(txt) == len(set(txt))  



# part 1
for t in dat:
    for i in range(len(t)-4):
        if checkMarker(t[i:i+4]):
            print(i+4)
            break



# part 2
for t in dat:
    for i in range(len(t)-14):
        if checkMarker(t[i:i+14]):
            print(i+14)
            break


