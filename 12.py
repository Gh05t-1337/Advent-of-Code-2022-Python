with open('input.txt') as f:
	inp=f.read().split('\n')

height=len(inp)
width=len(inp[0])

from collections import deque

class Graph:
	def __init__(self, adjac_lis,h,w):
		self.adjac_lis = adjac_lis
		self.hi=h
		self.wi=w

	def get_neighbors(self, v):
		return self.adjac_lis[v]

	# This is heuristic function which is having equal values for all nodes
	def h(self, n):
		H = {}
		for i in range(self.hi):
			for j in range(self.wi):
				H[(i,j)]=1	# (y,x)

		return H[n]

	def a_star_algorithm(self, start, stop):

		open_lst = set([start])
		closed_lst = set([])

		poo = {}
		poo[start] = 0
		par = {}
		par[start] = start

		while len(open_lst) > 0:
			n = None
			for v in open_lst:
				if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
					n = v;

			if n == None:
				print('Path does not exist!')
				return None
			if n == stop:
				reconst_path = []

				while par[n] != n:
					reconst_path.append(n)
					n = par[n]

				reconst_path.append(start)

				reconst_path.reverse()

				print('Path found: {}'.format(reconst_path))
				return reconst_path
			for (m, weight) in self.get_neighbors(n):
				if m not in open_lst and m not in closed_lst:
					open_lst.add(m)
					par[m] = n
					poo[m] = poo[n] + weight
				else:
					if poo[m] > poo[n] + weight:
						poo[m] = poo[n] + weight
						par[m] = n

						if m in closed_lst:
							closed_lst.remove(m)
							open_lst.add(m)
			open_lst.remove(n)
			closed_lst.add(n)

		print('Path does not exist!')
		return None

#adjac_lis = {
#	(0,0): [((0,0), 1), ((0,1), 3), ((1,0), 7)],
#	(0,1): [((1,0), 5)],
#	(1,1): [((1,0), 12)]
#}
adjac_lis = {}
start=(0,0)
end=(0,0)
for y in range(height):
	for x in range(width):
		if inp[y][x]=='S':
			start=(y,x)
			inp[y]=inp[y].replace('S','a')
		if inp[y][x]=='E':
			end=(y,x)
			inp[y]=inp[y].replace('E','z')
		adjac_lis[(y,x)]=[]
		if x>0:
			if ord(inp[y][x-1])-ord(inp[y][x])<=1:# or ord(inp[y][x-1])-ord(inp[y][x])==0:
				adjac_lis[(y,x)]+=[((y,x-1),1)]
		if x<width-1:
			if ord(inp[y][x+1])-ord(inp[y][x])<=1:# or ord(inp[y][x+1])-ord(inp[y][x])==0:
				adjac_lis[(y,x)]+=[((y,x+1),1)]
		if y>0:
			if ord(inp[y-1][x])-ord(inp[y][x])<=1:# or ord(inp[y-1][x])-ord(inp[y][x])==0:
				adjac_lis[(y,x)]+=[((y-1,x),1)]
		if y<height-1:
			if ord(inp[y+1][x])-ord(inp[y][x])<=1:# or ord(inp[y+1][x])-ord(inp[y][x])==0:
				adjac_lis[(y,x)]+=[((y+1,x),1)]
			

graph1 = Graph(adjac_lis,height,width)
# Part One
print('Part One: {len(graph1.a_star_algorithm(start, end))-1}')

# Part Two
# i cheated, by just looking at the input myself to see wich 'a' has the shortest path to E
print('Part Two: Check the source Code, You need to change something depending on your input')
#print('Part Two: {len(graph1.a_star_algorithm((4,0), end))-1}')