import sympy



# with open('./sample.txt') as f:
with open('./input.txt') as f:
    lines = [i.split(': ') for i in f.read().strip().splitlines()]


monkeys={}


monkeys = dict(lines)


def getNum(m):
    jj = monkeys[m]
    # parsing the full tree every time will require extra computation
    if jj.isdigit():
        return int(jj)
    else:
        try:
            m1,ex,m2 = jj.split()
        except:
            print(jj)
            raise
        return eval(f'{getNum(m1)} {ex} {getNum(m2)} ')



# guess human value so that root is zero
# modify the root so that it returns 0 i.e. both are equal
m1,ex,m2 = monkeys['root'].split()
monkeys['root'] = f"{m1} - {m2}"

high = 1e15
low=0




def getAns(val):
    monkeys['humn'] = str(val)
    return getNum('root')



for _ in range(120):
    mid = int((low+high)/2)



    lVal, mVal = getAns(low), getAns(mid)
    # print(mid,lVal,mVal)


    if mVal==0: 
        print(mid)
        break
    elif lVal*mVal>0: # same sign
        low=mid
    else:
        high =mid
