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
		boundz.append(category)
		validAreas.append(boundz)

print(tickets)
print(validAreas)

validtickets = []

# sort out invalid tickets
for ticket in tickets:
	tvalid = True
	for val in ticket:
		valid = False
		for area in validAreas:
			if area[0]<=int(val)<=area[1]:
				valid = True
				break;
		if not valid:
			tvalid = False
	if tvalid:
		validtickets.append(ticket)

print("valid:",validtickets)

cols = len(myticket)
rows = len(validtickets)

colIds = {} #fieldName, column id

for c in range(cols):
	for r in range(rows):
		#print(r,c)
		field = validtickets[r][c]
		# compare to validarea and if all columns are in range, this is the column of choice -> then log to colIds
		#print(areas)
