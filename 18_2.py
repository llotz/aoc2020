import re
lines = open("18in.txt").read().split("\n")


class num(int):
	def __sub__(self, b):
		return num(int(self)*int(b))
	
	def __add__(self, b):
		return num(int(self)+int(b))
	
	def __mul__(self, b):
		return num(int(self)+int(b))

s=0

for line in lines:
	line = line.replace('*', '-')
	line = line.replace('+', '*')
	line = re.sub("(\d+)", r'num(\1)', line)
	s += eval(line)

print(s)