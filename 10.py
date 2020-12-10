def getThreeHigherOrNext(list,currentValue):
	searchedVal = currentValue+3
	for val in list:
		if (val > currentValue and abs(currentValue-val)<abs(searchedVal-val)):
			searchedVal = val
	return searchedVal


adapters=[int(i) for i in open("10in.txt").read().split('\n')]

out=0
input=max(adapters)+3

print ("input:",input)

stepsofthree = 0
stepsofone = 0

while out < input-3:
	nextAdapter = getThreeHigherOrNext(adapters, out)
	if nextAdapter-out == 3:
		stepsofthree+=1
	if nextAdapter-out == 1:
		stepsofone+=1
	out=nextAdapter
stepsofthree+=1 #for last difference
print(stepsofthree, "x", stepsofone, "=", stepsofone*stepsofthree)