with open('./sample.txt') as f:
    txt = f.read()


monkeys = []
for t in txt.split('Monkey')[1:]:
    mon = {}
    tt = t.split('\n')
    it = tt[1].replace('Starting items: ','')
    op = tt[2].replace('  Operation: new = ','')
    test = tt[3].replace('  Test: divisible by ','')
    testCase1 = tt[4].replace('If true: throw to monkey','')
    testCase2 = tt[5].replace('If false: throw to monkey','')

    mon['items'] = eval(f'[{it}]')
    mon['op'] = eval(f'lambda old : {op}')
    mon['test'] = eval(f'lambda x: {testCase1} if x%{test}==0 else {testCase2}')
    mon['div'] = int(test)
    mon['count']=0
    monkeys.append(mon)


# part 1 ---------
for k in range(20):
    for i,monkey in enumerate(monkeys):
        for it in monkey['items']:
            newWorry = monkey["op"](it)//3
            newMonkey = monkey['test'](newWorry)
            monkeys[newMonkey]['items'].append(newWorry)
            monkeys[i]["count"] +=1
        monkey['items']=[]



mBus = [m['count'] for m in monkeys]
a,b = sorted(mBus)[-2:]
print(a*b)


# part 2 --------------------
## "you'll need to find another way to keep your worry levels manageable"
# otherwise the value will blow up, and the problem is unsolvable in polynomial time
modifier = 1
for m in monkeys:
    modifier *= m['div']


for k in range(10000):
    if k%1000==0:
        print(k,[m['count'] for m in monkeys])
    for i,monkey in enumerate(monkeys):
        for it in monkey['items']:
            newWorry = monkey["op"](it)%modifier
            newMonkey = monkey['test'](newWorry)
            monkeys[newMonkey]['items'].append(newWorry)
            monkeys[i]["count"] +=1
        monkey['items']=[]



mBus = [m['count'] for m in monkeys]
a,b = sorted(mBus)[-2:]
print(a*b)
