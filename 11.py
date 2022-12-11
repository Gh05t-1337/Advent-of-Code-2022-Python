with open('input.txt','r') as f:
	inp=f.read().split('\n\n')

# Part One
monkeys=[]
ops=[]
for m in inp:
	lins=m.split('\n')
	monkeys+=[[int(i) for i in ''.join(lins[1].split()[2:]).split(',')]]
	ops+=[[lins[2].split()[4],lins[2].split()[5],lins[3].split()[3],lins[4].split()[5],lins[5].split()[5]]]

inspected=[0]*len(monkeys)
for _ in '*'*20:
	for i,op in zip(range(len(monkeys)),ops):
		for _ in '*'*len(monkeys[i]):
			if op[1]=='old':
				new=(monkeys[i][0]**2) if op[0]=='*' else 2*monkeys[i][0]
			else:
				new=(monkeys[i][0]*int(op[1])) if op[0]=='*' else monkeys[i][0]+int(op[1])
			new//=3
			if new%int(op[2])==0:
				monkeys[int(op[3])]+=[new]
			else:
				monkeys[int(op[4])]+=[new]
			monkeys[i].pop(0)
			inspected[i]+=1
print(f'Part One: {sorted(inspected)[-2]*sorted(inspected)[-1]}')


# Part Two
mod=1
for m in ops:
	mod*=int(m[2])

monkeys=[]
for m in inp:
	lins=m.split('\n')
	monkeys+=[[int(i) for i in ''.join(lins[1].split()[2:]).split(',')]]

inspected=[0]*len(monkeys)

for _ in '*'*10000:
	for i,op in zip(range(len(monkeys)),ops):
		for _ in '*'*len(monkeys[i]):
			if op[1]=='old':
				new=(monkeys[i][0]**2) if op[0]=='*' else 2*monkeys[i][0]
			else:
				new=(monkeys[i][0]*int(op[1])) if op[0]=='*' else monkeys[i][0]+int(op[1])
			new%=mod
			if new%int(op[2])==0:
				monkeys[int(op[3])]+=[new]
			else:
				monkeys[int(op[4])]+=[new]
			monkeys[i].pop(0)
			inspected[i]+=1

print(f'Part Two: {sorted(inspected)[-2]*sorted(inspected)[-1]}')
