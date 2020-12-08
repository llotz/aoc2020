import os
import re

instructions = open("8in.txt").read().split("\n")
changedparameter = 0

while changedparameter < len(instructions):
	accumulator = 0
	executedInstructions = []
	nextInstruction = 0
	tempInstructions = instructions.copy()
	print(changedparameter)
	if "nop" in tempInstructions[changedparameter]:
		tempInstructions[changedparameter] = tempInstructions[changedparameter].replace("nop", "jmp")
	elif "jmp" in tempInstructions[changedparameter]:
		tempInstructions[changedparameter] = tempInstructions[changedparameter].replace("jmp", "nop")
	else:
		changedparameter += 1
		continue
	while nextInstruction not in executedInstructions and nextInstruction != len(instructions):
		currentInstruction = nextInstruction
		instruction = tempInstructions[nextInstruction]
		inst = instruction.split(' ')[0]
		arg = int(instruction.split(' ')[1])
		if inst == "acc":
			accumulator += arg
			nextInstruction += 1
		elif inst == "jmp":
			nextInstruction += arg
		elif inst == "nop":
			nextInstruction += 1
		executedInstructions.append(currentInstruction)
	if nextInstruction == len(instructions):
		print("YEEEES")
		break
	
	changedparameter += 1

print(executedInstructions , " | ", nextInstruction)
print(accumulator)