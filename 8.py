with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
def isVisible(tr):
	left=True;right=True
	for x in range(tr[0]):
		if inp[tr[1]][x]>=inp[tr[1]][tr[0]]:
			left=False;break
	for x in range(tr[0]+1,len(inp[0])):
		if inp[tr[1]][x]>=inp[tr[1]][tr[0]]:
			right=False;break

	up=True;down=True
	for y in range(tr[1]):
		if inp[y][tr[0]]>=inp[tr[1]][tr[0]]:
			up=False;break
	for y in range(tr[1]+1,len(inp)):
		if inp[y][tr[0]]>=inp[tr[1]][tr[0]]:
			down=False;break
	return up or left or down or right

counter=0
for x in range(len(inp[0])):
	for y in range(len(inp)):
		counter+=isVisible([x,y])*1

print(f'Part One: {counter}')

# Part Two
def scenicScore(tr):
	left=0;right=0
	for x in range(tr[0]-1,-1,-1):
		left+=1
		if inp[tr[1]][x]>=inp[tr[1]][tr[0]]:
			break
	for x in range(tr[0]+1,len(inp[0])):
		right+=1
		if inp[tr[1]][x]>=inp[tr[1]][tr[0]]:
			break

	up=0;down=0
	for y in range(tr[1]-1,-1,-1):
		up+=1
		if inp[y][tr[0]]>=inp[tr[1]][tr[0]]:
			break
	for y in range(tr[1]+1,len(inp)):
		down+=1
		if inp[y][tr[0]]>=inp[tr[1]][tr[0]]:
			break	
	return up*left*down*right

best_scene=0
for x in range(len(inp[0])):
	for y in range(len(inp)):
		scene=scenicScore([x,y])
		if scene>best_scene:
			best_scene=scene

print(f'Part Two: {best_scene}')

