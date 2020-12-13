import operator

input = open("13in.txt").read().split("\n")
busses = input[1].split(',')
bussesNumOnly = [int(i) for i in input[1].replace("x,", "").split(',')]

time = 1
left = False

res = 0

values = {}
for i,v in enumerate(busses):
	if v.isnumeric():
		values[int(v)]=int(i)

values = dict(sorted(values.items(), key=operator.itemgetter(1),reverse=True))

print(values)

runningProduct = 1
add = 0

for v in values:
	while (add+values[v]) % int(v) != 0:
		add += runningProduct
	runningProduct *= int(v)
	print("Sum so far:", add, "Product so far:", runningProduct)

print(runningProduct, "|", add)