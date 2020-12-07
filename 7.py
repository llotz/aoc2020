import os
import re

rules = open("7in.txt", "r").readlines()
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
		if bag == search:
			hits += 1
		else:
			if deepsearch(bags[bag][0], search) > 0:
				hits += 1
	return hits

def deepsearch(bagname, search):
	hits = 0
	for bag in bags[bagname]:
		if search == bag[0]:
			hits += 1
	return hits


search("shiny gold bag")




print(result)