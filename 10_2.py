import sys
#sys.setrecursionlimit(5000)

adapters=[int(i) for i in open("10in.txt").read().split('\n')]

cache = {}
def solve(i):
	if i==len(adapters)-1:
		return 1
	if i in cache:
		return cache[i]
	ans = 0
	for j in range(i+1, len(adapters)):
		if adapters[j]-adapters[i]<=3:
			ans += solve(i)
	cache[i] = ans
	return ans


out=0
input=max(adapters)+3
adapters.append(0)
adapters.append(input)
adapters.sort()


print(solve(0))
