with open('input.txt','r') as f:
	inp=f.read()

# Part One
ls=[]
for i in range(len(inp)):
	ls+=[inp[i]]
	if len(ls)>4:
		del ls[0]
	if len(ls)==4 and len(list(set(ls)))==4:
		print(f'Part One: {i+1}')
		break

# Part Two
ls=[]
for i in range(len(inp)):
	ls+=[inp[i]]
	if len(ls)>14:
		del ls[0]
	if len(ls)==14 and len(list(set(ls)))==14:
		print(f'Part Two: {i+1}')
		break