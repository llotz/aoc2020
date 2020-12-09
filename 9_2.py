numbers = open("9in.txt").read().split('\n')
index = 0
target = 88311122

def sumFirstAndLastInListWhichSumTo(list, x):
	idx=0
	for val in list:
		subList = list[idx:]
		buffer = 0
		smallest = 0
		largest = 0
		for n in subList:
			
			buffer += int(n)
			if int(n) < smallest or smallest == 0:
				smallest=int(n)
			if int(n) > largest or largest == 0:
				largest=int(n)
			if buffer == x:
				print(smallest, "|", largest)
				return int(smallest)+int(largest)
			if buffer > x:
				continue
		idx+=1
				
						

print(sumFirstAndLastInListWhichSumTo(numbers, target))