with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
sum=0
X=1
cyc=0
check=20
cyclesX=[] #preperation for part two
for line in inp:
	if line.split()[0]=='addx':
		cyc+=2
		cyclesX+=[X]*2 #preperation for part two
		if cyc>=check:
			sum+=check*X
			check+=40
		X+=int(line.split()[1])
	else:
		cyc+=1
		cyclesX+=[X] #preperation for part two
		if cyc>=check:
			sum+=check*X
			check+=40
			
print(f'Part One: {sum}')

# Part Two
print('\nPart Two:')
for i in range(len(cyclesX)):
	if i%40==0 and i!=0:
		print()
	bol=(i%40)==cyclesX[i]-1 or (i%40)==cyclesX[i] or (i%40)==cyclesX[i]+1
	print('#'*bol+'.'*(not bol),end='')
	