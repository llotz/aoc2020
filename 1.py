import os

lines = open('1in.txt').read().split('\n')

for l in lines:
	if l == '':
		continue
	for m in lines:
		if m == '':
			continue
		for n in lines:
			if n == '': 
				continue;
			if int(l) + int(m) + int(n) == 2020:
				res = int(l) * int(m) * int(n)
				print(res);
