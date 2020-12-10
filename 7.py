import os
import re

rules = open("7in.txt", "r").read().split('\n')
result = 0

bags = {}
containers = []

for rule in rules:
	contains = rule.replace(".", "").split("contain ")[1]
	bagname = rule.split("s contain")[0]
	containedbags = []
	for containedbag in contains.split(", "):
		subbagcount = containedbag.split(" ")[0]
		if subbagcount == "no":
			continue
		subbagname = " ".join(containedbag.split(" ")[1:]).rstrip("s")
		containedbags.append([subbagname, subbagcount])
	bags[bagname] = containedbags

#print(bags)

def search(search):
	hits = 0
	for bag in bags:
		for containedbag in bags[bag]:
			if containedbag[0] == search:
				addToContainers(bag)
				hits += 1
				break	
		if deepsearch(containedbag[0], search) > 0:
			hits += 1
	return hits

def deepsearch(bagname, search):
	#print("deepsearching:",bagname)
	hits = 0
	if len(bags[bagname]) == 0:
		return 0
	for containedbag in bags[bagname]:
		if containedbag[0] == search:
			addToContainers(bagname)
			hits += 1
			break
		if deepsearch(containedbag[0], search) > 0:
			hits += 1
	return hits

def addToContainers(bagname):
	if bagname not in containers:
		containers.append(bagname)
		print(bagname)

print(search("shiny gold bag"))
print(len(containers))