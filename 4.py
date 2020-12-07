import re

lines = open("4in.txt", "r").read().split("\n\n")
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passedPasses = 0

for line in lines:
	line = line.replace("\n", " ")
	optionsValid = 0
	for r in required:
		if r in line:
			optionsValid += 1
		if optionsValid == 7:
			optionsValid = 0
			fields = line.split(" ")
			for field in fields:
				if field == "":
					continue
				f = field.split(':')
				val = f[1]
				if f[0]=="byr" and int(val)<=2002 and int(val)>=1920:
					optionsValid += 1
				if f[0]=="iyr" and int(val)<=2020 and int(val)>=2010:
					optionsValid += 1
				if f[0]=="eyr" and int(val)<=2030 and int(val)>=2020:
					optionsValid += 1
				if f[0]=="hgt" and ((val.endswith("cm") and int(val[0:-2]) <= 193 and int(val[0:-2]) >= 150) or (val.endswith("in") and int(val[0:-2]) <= 76 and int(val[0:-2]) >= 59)):
					optionsValid += 1
				if f[0]=="hcl" and re.match(r"#[a-fA-F0-9]{6}", val):
					optionsValid += 1
				if f[0]=="ecl" and val in ["amb","blu", "brn" ,"gry", "grn", "hzl", "oth"]:
					optionsValid += 1
				if f[0]=="pid" and re.match(r"[0-9]{9}", val):
					optionsValid += 1
			print(optionsValid);
			if optionsValid == 7:		
				passedPasses += 1
print(passedPasses)
