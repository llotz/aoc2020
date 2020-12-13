input = open("13in.txt").read().split("\n")
arrival = int(input[0])
busses = [int(i) for i in input[1].replace("x,", "").split(',')]

time = arrival
left = False

res = 0

while not left:
	#print("time",time)
	for bus in busses:
		if time % bus == 0:
			res = bus * (time-arrival)
			left = True
	time += 1

print(res)