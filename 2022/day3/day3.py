import numpy as np 

# with open('sample.txt') as f:
with open('input.txt') as f:
    dat = f.read().strip().splitlines()



def priorityVal(let:str):
    return ord(let) - (96 if let.islower() else 38)


s = 0 

for t in dat:
    l = len(t)//2
    a,b = t[:l], t[l:]
    for i in a:
        if i in b:
            s += priorityVal(i)
            break # assume one occurance
print(s)



s = 0 

for i in range(len(dat)//3):
    a = dat[i*3]
    b = dat[i*3+1]
    c = dat[i*3+2]
    for i in a: 
        if (i in b) and (i in c):
            s+=priorityVal(i)
            break
print(s)
