import os
import re

groups = open("6in.txt", "r").read().split('\n\n')
result = 0

for group in groups:
	if group == "":
		continue
	persons = group.split("\n")
	firstPerson = list(persons[0])
	print(persons)
	print(persons[0])
	for person in persons[1:]:
		localPerson = firstPerson.copy() # I needed to to an implementation in C# to figure out this is necessary.
		for item in localPerson:
			if item not in list(person):
				firstPerson.remove(item)
	print(firstPerson)
	print(len(firstPerson))
	result += len(firstPerson)

print("result:",result)