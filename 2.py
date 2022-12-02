with open('input.txt','r') as f:
	inp=f.read()

# Part 1
score=0
for line in inp.split('\n'):
	op=ord(line[0])-64
	pl=ord(line[2])-87

	if pl-op==0: #draw
		score+=3
	if (pl-op)%3==1: #win
		score+=6

	score+=pl

print('Part One: '+str(score))

# Part 2
score=0
for line in inp.split('\n'):
	op=ord(line[0])-65
	pl=ord(line[2])-88

	score+=pl*3+(op+(pl-1))%3+1

print('Part Two: '+str(score))


