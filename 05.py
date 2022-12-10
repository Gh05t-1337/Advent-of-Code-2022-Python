import copy
with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Stacks to list
stacks=[[] for _ in range((len(inp[0])-1)//4+1)]
ind=[x for x in range(len(inp)) if inp[x] == ''] [0]
prestacks=list(map(list,zip(*inp[::-1][-1*ind+1:])))


for i in range(1,len(prestacks),4):
	while ' ' in prestacks[i]:	
		prestacks[i].remove(' ')
	stacks[(i-1)//4]=prestacks[i]

original_stacks=copy.deepcopy(stacks)
#print(original_stacks)
# Part One
for line in inp[ind+1:]:
	coms=line.replace('move ','').replace(' from ',' ').replace(' to ',' ').split()
	for _ in '*'*int(coms[0]):
		stacks[int(coms[2])-1]+=[stacks[int(coms[1])-1][-1]]
		stacks[int(coms[1])-1].pop()

print(''.join([stack[-1] for stack in stacks]))


# Part Two
stacks=copy.deepcopy(original_stacks)

for line in inp[ind+1:]:
	coms=line.replace('move ','').replace(' from ',' ').replace(' to ',' ').split()

	stacks[int(coms[2])-1]+=stacks[int(coms[1])-1][-1*int(coms[0]):]
	stacks[int(coms[1])-1]=stacks[int(coms[1])-1][:-1*int(coms[0])]
	#input(line+'\n'+str(stacks))

print(''.join([stack[-1] for stack in stacks]))



