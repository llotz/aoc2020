import os
import re

rules = open("7in.txt", "r").read().split('\n')
result = 0

bags = {}

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

def search(search):
	hits = 0
	for bag in bags:
		for containedbag in bags[bag]:
			if containedbag[0] == search:
				hits += 1
			else:
				if deepsearch(containedbag[0], search) > 0:
					hits += 1
	return hits

def deepsearch(bagname, search):
	hits = 0
	if len(bags[bagname]) == 0:
		return hits
		for containedbag in bags[bagname]:
			if containedbag[0] == search:
				hits += 1
			else:
				if deepsearch(containedbag[0], search) > 0:
					hits += 1
	return hits


print(search("shiny gold bag"))
