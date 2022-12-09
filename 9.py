with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
dic={}
posH=(0,0)
posT=(0,0)
dic[(0,0)]=1
for line in inp:
	vec=(1*((a:=line.split()[0])=='R')-1*(a=='L'),-1*(a=='D')+1*(a=='U'))
	for i in range(int(line.split()[1])):
		posH=(posH[0]+vec[0],posH[1]+vec[1])
		if abs(posH[0]-posT[0])>1 or abs(posH[1]-posT[1])>1:
			if posH[0]==posT[0]:
				posT=(posT[0],(posH[1]-posT[1])//2+posT[1])
			elif posH[1]==posT[1]:
				posT=((posH[0]-posT[0])//2+posT[0],posT[1])
			elif abs(posH[0]-posT[0])>1:
				posT=((posH[0]-posT[0])//2+posT[0],(posH[1]-posT[1])+posT[1])
			else:
				posT=((posH[0]-posT[0])+posT[0],(posH[1]-posT[1])//2+posT[1])
			dic[posT]=1
print(f'Part One: {len(dic.keys())}')

# Part Two
snake=[(0,0)]*10
dic={}

for line in inp:
	vec=(1*((a:=line.split()[0])=='R')-1*(a=='L'),-1*(a=='D')+1*(a=='U'))
	for i in range(int(line.split()[1])):
		snake[0]=(snake[0][0]+vec[0],snake[0][1]+vec[1])
		for i in range(len(snake)-1):
			if abs(snake[i][0]-snake[i+1][0])>1 or abs(snake[i][1]-snake[i+1][1])>1:
				if snake[i][0]==snake[i+1][0]:
					snake[i+1]=(snake[i+1][0],(snake[i][1]-snake[i+1][1])//2+snake[i+1][1])
				elif snake[i][1]==snake[i+1][1]:
					snake[i+1]=((snake[i][0]-snake[i+1][0])//2+snake[i+1][0],snake[i+1][1])
				elif abs(snake[i][0]-snake[i+1][0])>1:
					snake[i+1]=((snake[i][0]-snake[i+1][0])//2+snake[i+1][0],(snake[i][1]-snake[i+1][1])+snake[i+1][1])
				else:
					snake[i+1]=((snake[i][0]-snake[i+1][0])+snake[i+1][0],(snake[i][1]-snake[i+1][1])//2+snake[i+1][1])
		dic[snake[-1]]=1

print(f'Part Two: {len(dic.keys())}')