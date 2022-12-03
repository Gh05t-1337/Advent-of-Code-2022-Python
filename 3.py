with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
#one-liner
#sum=0;[sum:=sum+[ord(i.lower())-96+i.isupper()*26 for i in set(l[:len(l)//2])&set(l[len(l)//2:])][0] for l in inp];print(sum)

sum=0
for line in inp:
	sum+=[ord(i.lower())-96+i.isupper()*26 for i in set(line[:len(line)//2])&set(line[len(line)//2:])][0]

print(f'Part One: {sum}')


# Part Two
sum=0
for i in range(len(inp)//3):
	sum+=[ord(c.lower())-96+c.isupper()*26 for c in set(inp[3*i])&set(inp[3*i+1])&set(inp[3*i+2])][0]

print(f'Part Two: {sum}')