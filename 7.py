import sys
#sys.setrecursionlimit(5000)

lines = open("7in.txt").read().split('\n')

bags = {}
for line in lines:
	l = line.split(" contain ")
	bagname = l[0].replace(" bags", "")
	contains = []
	bags[bagname] = contains
	if l[1].split(' ')[0] == "no":
		continue
	for c in l[1].split(','):
		val = c.rstrip('.').rstrip(' bags').lstrip()
		amount = val.split(" ")[0]
		name = val[1:].strip()
		contains.append(name)

goldContainers = []
doneContainers = []

def addToGoldContainers(name):
	if name not in goldContainers:
		goldContainers.append(name)

def addToDoneContainers(name):
	if name not in doneContainers:
		doneContainers.append(name)

def search(k,s):
	print("called",k)
	occ = 0
	if k in doneContainers:
		return 0;
	if k in bags:
		if len(bags[k]) == 0:
			addToDoneContainers(k)
			return 0

	for i in bags.keys():
		for sub in bags[i]:
			print(sub)
			if sub == s:
				addToDoneContainers(i)
				addToGoldContainers(i)
				occ += 1
				print(i)
			else:
				if search(sub, s)>0:
					addToDoneContainers(i)
					addToGoldContainers(i)
	return occ
print(search("", "shiny gold"))