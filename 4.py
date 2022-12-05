with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
sum=0
for line in inp:
	elfs=line.split(',')
	elf1=range(int(elfs[0].split('-')[0]),int(elfs[0].split('-')[1])+1)
	elf2=range(int(elfs[1].split('-')[0]),int(elfs[1].split('-')[1])+1)
	if set(elf1)&set(elf2)==set(elf1) or set(elf1)&set(elf2)==set(elf2):
		sum+=1
print(f'Part One: {sum}')

# Part Two
sum=0
for line in inp:
	elfs=line.split(',')
	elf1=range(int(elfs[0].split('-')[0]),int(elfs[0].split('-')[1])+1)
	elf2=range(int(elfs[1].split('-')[0]),int(elfs[1].split('-')[1])+1)
	if set(elf1)&set(elf2)!=set([]):
		sum+=1
print(f'Part Two: {sum}')