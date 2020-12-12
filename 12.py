instructions = open("12in.txt").read().split("\n")

north = 0
east = 0

direction = 90 #heading east

directions = {
	0: "N",
	90: "E",
	180: "S",
	270: "W"
}

def moveDirection(c, d):
	print(c,"|",d, "|",direction)
	global north
	global east
	if c == "E":
		east += d
	elif c == "N":
		north += d
	elif c == "S":
		north -= d
	elif c == "W":
		east -= d

for inst in instructions:
	print(inst)
	c = inst[0]
	d = int(inst[1:])
	if c in "ENSW":
		moveDirection(c, d)
	elif(c =="R"):
		direction += d
		if direction >= 360:
			direction = direction % 360
	elif(c == "L"):
		direction -= d
		if direction < 0:
			direction += 360
	elif(c == "F"):
		moveDirection(directions[direction], d)

print(abs(north), "|",abs(east), "=",abs(north)+abs(east))