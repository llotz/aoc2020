numbers = open("9in.txt").read().split('\n')
index = 0

def anyTwoInListSumTo(list, x):
	for n in list:
		for m in list:
			if n != m and int(n)+int(m) == int(x):
				return True
	return False

for number in numbers[25:]:
	highestPreambleIndex = index+25
	preamble = numbers[index:highestPreambleIndex]
	if not anyTwoInListSumTo(preamble, number):
		print("booooom, that's your fookin result.. maybe:", number)
		break;
	index += 1