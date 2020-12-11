seatmap = open("11in.txt").read().split('\n')

lines=len(seatmap)
cols=len(seatmap[0])

def seats_next_occupied(x, y):
	#print("x,y",x,y)
	count = 0
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if [x,y] != [i,j] and i>=0 and j>=0 and i < cols and j < lines and seatmap[j][i] == '#':
				count+=1
				#print(i,j)
	#if count > 0:
		#print("count:",count)
	return count

def count_seats(char):
	count = 0
	for line in seatmap:
		count += line.count(char)
	return count

changes = True
while changes:
	changes = False
	newmap = seatmap.copy()
	#for line in seatmap:
		#print(line)
	#print("----------")
	for y in range(0, len(seatmap)):
		for x in range(0, len(seatmap[y])):
			if seatmap[y][x] == "#" and seats_next_occupied(x,y)>3:
				l = list(newmap[y])
				l[x] = "L"
				newmap[y] = ''.join(l)
				#print("- x:",x,"y:",y)
				changes = True
			if seatmap[y][x] == "L" and seats_next_occupied(x,y)==0:
				l = list(newmap[y])
				l[x] = "#"
				newmap[y] = ''.join(l)
				#print("+ x:",x,"y:",y)
				changes = True
	seatmap = newmap.copy()
	

print(count_seats('L'))
print(count_seats('#'))