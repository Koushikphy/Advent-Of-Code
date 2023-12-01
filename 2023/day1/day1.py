# file = './sample1.txt'
file = './input.txt'


digits = '0123456789'

ss = 0 
with open(file) as f:
    txt = f.read()
    for line in txt.splitlines():
        # print(line)
        arr = []
        for d in digits:
            if (ind:=line.find(d))!=-1:
                arr.append((ind,d))
            if (ind:=line.rfind(d))!=-1:
                arr.append((ind,d))
        arr.sort()
        # print(arr)

        ss+= int(arr[0][1]+arr[-1][1])

print(ss)



# part 2

file = './sample.txt'
file = './input.txt'

sdigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ss = 0 
with open(file) as f:
    txt = f.read()
    for line in txt.splitlines():
        # print(line)
        arr = []
        for d in digits:
            if (ind:=line.find(d))!=-1:
                arr.append((ind,d))
            if (ind:=line.rfind(d))!=-1:
                arr.append((ind,d))
        for i,d in enumerate(sdigits,start=1):
            if (ind:=line.find(d))!=-1:
                arr.append((ind,str(i)))
            if (ind:=line.rfind(d))!=-1:
                arr.append((ind,str(i)))
        arr.sort()
        # print(arr)

        ss+= int(arr[0][1]+arr[-1][1])

print(ss)



