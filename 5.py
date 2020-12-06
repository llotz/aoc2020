lines = open("5in.txt", "r").read().split("\n")
highest = 0
takenseats = []
for line in lines:
	if line == "":
		continue
	row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
	col = int(line[-3:].replace('L', '0').replace('R', '1') ,2)
	seatid = row * 8 + col
	if seatid > highest:
		highest = seatid
	takenseats.append(seatid)
for x in range(1,max(takenseats)):
	if x not in takenseats:
		print(x)
takenseats.sort()
#print(takenseats)

