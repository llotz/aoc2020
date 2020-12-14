r = open("14in.txt").read().split('\n')

memory = {}
mask = ""


def applyMask(mask, value):
    for i, v in enumerate(mask):
        if v != "0":
            value = value[:i]+v+value[i+1:]
    return value


def floatMeBaby(adress):
    adresses = []
    amount = adress.count('X')

    rawbinary = "1"*amount
    increasor = int(rawbinary, 2)

    print(increasor)

    for i in range(0, increasor+1):
        binary = "{0:b}".format(i).zfill(len(rawbinary))
        tmpAdress = adress
        for r in binary:
            tmpAdress = tmpAdress.replace('X', r, 1)
        adresses.append(int(tmpAdress, 2))
    return adresses


for line in r:
    print(line)
    if line.startswith("mask = "):
        mask = line.split(" = ")[1]
        continue
    else:
        value = int(line.split(" = ")[1])
        adress = ("{0:b}".format(
            int(line.split("[")[1].split("]")[0]))).zfill(36)
        adress = applyMask(mask, adress)
        adresses = floatMeBaby(adress)

        for a in adresses:
            memory[a] = value
        print(adresses, value)

sum = 0

for m in memory:
    sum += memory[m]
print(sum)
