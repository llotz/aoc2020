import os

test = open("2in.txt", "r").read().split("\n")
validCount = 0
for i in test:
	if i == '':
		continue
	val = i.split(': ')[1]
	idx = i.split(': ')[0]
	c = idx.split(' ')[1]
	start = int(idx.split(' ')[0].split('-')[0])-1
	end = int(idx.split(' ')[0].split('-')[1])-1
	ct = val.count(idx.split(' ')[1])
	#ct >= int(idx.split(' ')[0].split('-')[0]) and ct <= int(idx.split(' ')[0].split('-')[1]) 
	print(i," ",validCount," ", start, " ", end, " ", val[start], " ", val[end])
	if(not (val[start]==c and val[end]==c) and (val[start]==c or val[end]==c)):
		validCount += 1
print(validCount)