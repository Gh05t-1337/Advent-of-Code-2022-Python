with open('input.txt','r') as f:
	inp=f.read().split('\n')

# Part One
# get total size of directory
def getSize(d):
	size=0
	for item in d:
		if type(d[item])==type(1):
			size+=d[item]
		else:
			size+=getSize(d[item])
	return size

# sum all directories with size<=100000
summe=0
def sumDirs(d):
	global summe
	for item in d:
		if type(d[item])!=type(1):
			siz=getSize(d[item])
			if siz<=100000:
				summe+=siz
			sumDirs(d[item])
	
# build tree. example tree: a={'/':{'a':{'e':{'i':584},'f':29116, 'g':2557, 'h.lst':62596}, 'b.txt': 14848584, 'c.dat':8504156,'d':{'j':4060174,'d.log':8033020,'d.ext':5626152,'k':7214296}}}
a={'/':{}}
curdir=a['/']
curpath=['/']
for line in inp[1:]:
	if line[:4]=='$ cd':
		newdir=line.split()[2]
		if newdir not in curdir and newdir!='..':
			curdir[newdir]={}
		if newdir=='..':
			curpath.pop()
			curdir=a
			for name in curpath:
				curdir=curdir[name]
		elif newdir=='/':
			curdir=a['/']
			curpath=['/']
		else:
			curdir=curdir[newdir]
			curpath+=[newdir]
	elif line.split()[0]=='dir':
		if line.split()[1] not in curdir:
			curdir[line.split()[1]]={}
	elif line.split()[0]!='$':
		curdir[line.split()[1]]=int(line.split()[0])

sumDirs(a)
print(f'Part One: {summe}')

# Part Two
USED=getSize(a['/'])	#used space
TOTAL=70000000		#total available space
NEEDED=30000000-(TOTAL-USED)	#space still needed

dirToDel=USED	#size of dir that should be deleted
def allDirSizes(d):
	global dirToDel
	for item in d:
		if type(d[item])!=type(1):
			siz=getSize(d[item])
			if siz>=NEEDED and siz<dirToDel:
				dirToDel=siz
			allDirSizes(d[item])
allDirSizes(a)
print(f'Part Two: {dirToDel}')


