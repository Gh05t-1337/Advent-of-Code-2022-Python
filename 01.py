with open("input.txt","r") as f:
	inp=f.read()

sums=[sum([int(i) for i in l.split('\n')]) for l in inp.split('\n\n')]

#following can be used, if "ValueError: invalid literal for int() with base 10: ''" occurs.
#sums=[sum([int(i) if any(map(str.isdigit, i)) else 0 for i in l.split('\n')]) for l in inp.split('\n\n')])[-3:]

sol1=max(sums)
sol2=sum(sorted(sums)[-3:])

print(f"Part One: {sol1}\nPart Two: {sol2}")
