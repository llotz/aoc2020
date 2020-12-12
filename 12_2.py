instructions = open("12in.txt").read().split("\n")

ship_north = 0
ship_east = 0

waypoint_north = 1
waypoint_east = 10

directions = {
	0: "N",
	90: "E",
	180: "S",
	270: "W"
}

def moveWaypoint(c, d):
	print(c,"|",d)
	global waypoint_north
	global waypoint_east
	if c == "E":
		waypoint_east += d
	elif c == "N":
		waypoint_north += d
	elif c == "S":
		waypoint_north -= d
	elif c == "W":
		waypoint_east -= d

def rotateWaypoint(dir, degrees):
	global waypoint_north
	global waypoint_east
	if dir == "R":
		for i in range(int(degrees/90)):
			temp = waypoint_north
			waypoint_north = waypoint_east-2*waypoint_east
			waypoint_east = temp
	else:
		for i in range(int(degrees/90)):
			temp = waypoint_east
			waypoint_east = waypoint_north-2*waypoint_north
			waypoint_north = temp
		

for inst in instructions:
	print(inst)
	c = inst[0]
	d = int(inst[1:])
	if c in "ENSW":
		moveWaypoint(c, d)
	elif(c =="R"):
		rotateWaypoint(c,d)
	elif(c == "L"):
		rotateWaypoint(c,d)
	elif(c == "F"):
		for i in range(d):
			ship_east += waypoint_east
			ship_north += waypoint_north

print(abs(ship_north), "|",abs(ship_east), "=",abs(ship_north)+abs(ship_east))