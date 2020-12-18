lines = open("18in.txt").read().split("\n")
equotations = []
for line in lines:
	line = line.replace("(", "( ").replace(")", " )")
	equotations.append(line.split(' '))


def createHeatmap(equotations):
	heatmap = {}
	for i,eq in enumerate(equotations):
		depth = 0
		depthT = []
		for e in eq:
			if e == "(":
				depth += 1
			depthT.append(depth)
			if e ==")":
				depth -= 1
		heatmap[i] = depthT
	return heatmap

def calc(eq):
	res = int(eq[0])
	for i,v in enumerate(eq[1:len(eq)-1]):
		if v == "+":
			res += int(eq[i+2])
		elif v == "*":
			res *= int(eq[i+2])
	return res
		

def solve(eq, heatmap):
	print("solve:",eq)
	solution = 0
	while True:
		maximum = max(heatmap)
		if maximum == 0:
			break
		maxrangeindices = []
		for i in range(len(heatmap)):
			if heatmap[i] == maximum and (eq[i]=="(" or eq[i]==")"):
				maxrangeindices.append(i)
		print(maxrangeindices)

		results = []
		for i in range(0,len(maxrangeindices),2):
			substr = eq[maxrangeindices[i]+1:maxrangeindices[i+1]]
			print(substr)
			localresult = calc(substr)
			print(localresult)
			results.append(localresult)
		
		for i in range(len(maxrangeindices)-1,0,-2):
			high = maxrangeindices[i]
			low = maxrangeindices[i-1]
			eq=eq[:low]+[results[int(i/2)]]+eq[high+1:]
			heatmap = heatmap[:low]+[heatmap[low]-1]+heatmap[high+1:]
			print(eq)
			print(heatmap)
	print(eq)
	return calc(eq)

heatmap = createHeatmap(equotations)
print(heatmap)
answer = 0
for i,eq in enumerate(equotations):
	answer += solve(eq, heatmap[i])
print(answer)