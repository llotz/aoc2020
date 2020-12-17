inp = open("16in.txt").read()

rawrules = [i.rstrip("\n") for i in inp.split("your ticket:")[0].replace("\n\n", "").split("\n")]
myticket = [i.rstrip("\n") for i in inp.split("your ticket:")[1].split("\n")[1].split(",")]
rawtickets = [i.rstrip("\n") for i in inp.split("nearby tickets:")[1].split("\n")]

tickets = []
for i in rawtickets:
	if i == "":
		continue
	lol = [int(x) for x in i.split(",")]
	tickets.append(lol)

validAreas = []

for r in rawrules:
	category = r.split(":")[0]
	rulez = r.split(": ")[1].split(" or ")
	areas = [] # I guess this is necessary for the second task
	for x in rulez:
		boundz = [int(i) for i in x.split('-')]
		areas.append(boundz[0])
		areas.append(boundz[1])
	areas.append(category)
	validAreas.append(areas)

print(tickets)
print(validAreas)

validtickets = []

# sort out invalid tickets
for ticket in tickets:
	tvalid = True
	for val in ticket:
		valid = False
		for area in validAreas:
			if area[0]<=val<=area[1] or area[2]<=val<=area[3]:
				valid = True
				break;
		if not valid:
			tvalid = False
	if tvalid:
		validtickets.append(ticket)

print("valid:",validtickets)
print("areas:",validAreas)

cols = len(myticket)
rows = len(validtickets)

print("cols:",cols, "rows:", rows)

colIds = {} #fieldName, column id
taken = []

for c in range(cols):
	for area in validAreas:
		isAllInRange = True
		for r in range(rows): #foreach row in column: is in range?
			field = validtickets[r][c]
			if area[0]<=field<=area[1] or area[2]<=field<=area[3]:
				print(r,c,"valid:",field,"in range:", area[0], area[1], "or", area[2], area[3])
			else:
				print(r,c,"not valid:",field,"in range:", area[0], area[1], "or", area[2], area[3])
				isAllInRange = False
				break
		# compare to validarea and if all columns are in range, this is the column of choice -> then log to colIds
		if isAllInRange:
			colIds[area[4]] = c
			break
		

print(colIds)