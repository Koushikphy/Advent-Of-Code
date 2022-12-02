import numpy as np 

with open('input.txt') as f:
    dat = f.read().strip().split('\n\n')


arr = np.array([sum([float(i) for i in d.split('\n')]) for d in dat] )

# part 1
print(np.max(arr))

# part 2
print(sum(np.sort(arr)[-3:]))