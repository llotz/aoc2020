input = open("13in.txt").read().split("\n")
busses = input[1].split(',')

time = 1
left = False

res = 0

while not left:
	works = 0
	#print(time)
	for i in range(len(busses)):
		if busses[i] == "x":
			works += 1
			continue
		if (time+i) % int(busses[i]) == 0:
			works += 1
	if works == len(busses):
		left = True
		res = time

	time += 1

print(res)