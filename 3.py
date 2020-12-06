lines = open("3in.txt", "r").read().split("\n")
highest = 0
takenseats = []

row = 0
col = 0
hits = 0
lineLength = len(lines[0])

while row < len(lines):
    line = lines[row]
    if line == "":
        continue

    if(lines[row][col % lineLength] == '#'):
        hits = hits + 1

    row = row + 2
    col = col + 1


print(hits)
