import re 

rx = re.compile(r'([A-Z][A-Z]|\d+)')

valveLayout = {}

# with open('./input.txt') as f:
with open('./sample.txt') as f:
    lines = f.read().strip().splitlines()
    for i in lines:
        lay = rx.findall(i)
        valveLayout[lay[0]]={
            'rate': int(lay[1]),
            'to':lay[2:]
        }


