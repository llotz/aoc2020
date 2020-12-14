r = open("14in.txt").read().split('\n')

memory = {}
mask = ""


def applyMask(mask, value):
    for i, v in enumerate(mask):
        if v != "X":
            value = value[:i]+v+value[i+1:]
    return value


for line in r:
    print(line)
    if line.startswith("mask = "):
        mask = line.split(" = ")[1]
        continue
    else:
        adress = line.split("[")[1].split("]")[0]
        value = ("{0:b}".format(int(line.split(" = ")[1]))).zfill(36)
        value = applyMask(mask, value)
        memory[adress] = value
        print(adress, value)

sum = 0

for m in memory:
    sum += int(memory[m], 2)
print(sum)
