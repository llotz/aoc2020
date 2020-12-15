numbers = [int(i) for i in open("15in.txt").read().split(",")]

print(numbers)

amountspoken = {}  # number, spokentime
lastspoken = {}  # number, turn
listspoken = [] # continuing number list

turn = 0
cachelast = 0

while True:
	turn += 1
	if turn <= len(numbers) and numbers[turn-1] not in lastspoken:
		lastspoken[numbers[turn-1]] = turn
		listspoken.append(numbers[turn-1])
		amountspoken[numbers[turn-1]] = 1
		print(numbers[turn-1])

	# next number = lastnumber Turn - previous turn spoken
	# if not appeared til last: next number = 0
	else: 
		lastNumber = listspoken[-1:][0]
		nextNumber=0
		#print(lastNumber)
		if amountspoken[lastNumber] > 1:
			lastTurn = turn-1
			prevTurn = len(listspoken) - 1 - listspoken[:-1][::-1].index(lastNumber)
			nextNumber = lastTurn-prevTurn
		lastspoken[nextNumber] = turn
		listspoken.append(nextNumber)
		if nextNumber in amountspoken:
			amountspoken[nextNumber] = amountspoken[nextNumber]+1
		else:
			amountspoken[nextNumber] = 1

		if turn == 2020:
			print("sol:",nextNumber)
			break;