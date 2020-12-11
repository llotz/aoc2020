from copy import deepcopy

seatmap = [list(s.strip()) for s in list(open("11in.txt").read().split('\n'))]

lines=len(seatmap)
cols=len(seatmap[0])

def seats_in_view_occupied(x, y):
	count = 0
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			yy = y + dy
			xx = x + dx
			if [y,x] != [yy, xx]:
				while 0<=xx<cols and 0<=yy<lines and seatmap[yy][xx] == '.':
					yy = yy+dy
					xx = xx+dx
				if 0<=xx<cols and 0<=yy<lines and seatmap[yy][xx] == '#':
					count+=1
	return count

def count_seats(char):
	count = 0
	for line in seatmap:
		count += line.count(char)
	return count


changes = True
while changes:
	changes = False
	newmap = deepcopy(seatmap)
	for y in range(0, len(seatmap)):
		for x in range(0, len(seatmap[y])):
			if seatmap[y][x] == "L" and seats_in_view_occupied(x,y)==0:
				newmap[y][x] = "#"
				#print("+ x:",x,"y:",y)
				changes = True
			if seatmap[y][x] == "#" and seats_in_view_occupied(x,y)>4:
				newmap[y][x] = "L"
				#print("- x:",x,"y:",y)
				changes = True
	seatmap = newmap
	#for line in seatmap:
	#	print("".join(line))
	#print("----------")

print(count_seats('#'))