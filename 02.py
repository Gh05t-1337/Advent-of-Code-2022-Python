with open('input.txt','r') as f:
	inp=f.read()

# Part 1
score=0
for line in inp.split('\n'):
	op=ord(line[0])-65	#A->0, B->1, C->2
	pl=ord(line[2])-87	#X->1, Y->2, Z->3

	score+=pl+((pl-op)%3)*3	

print('Part One: '+str(score))

# Part 2
score=0
for line in inp.split('\n'):
	op=ord(line[0])-65
	pl=ord(line[2])-88

	score+=pl*3+(op+(pl-1))%3+1

print('Part Two: '+str(score))
