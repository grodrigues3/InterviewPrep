import simplejson as json
import numpy as np
# 0: Left
# 1: Right
# 2: Up
# 3: Down

#type(game['board'])
#type( game['end'])
#type(game['start'])
#type(game['standing_crates'])
#type(game['toppled_crates'])

def solve_game(game, location, board_rep):
	if location == game['end']:
		print 'CUT! You Win!'
		return True
	for direction in range(1,4): 
		if can_move(location, direction, board_rep):
			[new_board, new_location] = move(game,location, direction, board_rep)
			solve_game(game, new_location, new_board)


def move(game, loc, direction, binary_board):
	[r,c] = loc
	if isStanding(loc):
		[new_board, new_loc] = topple(loc, direction, binary_board)
	if direction == 0: 
		return [r,c-1]
	elif direction == 1: return [r,c+1]
	elif direction == 2: return[r-1,c]
	elif direction == 3: return [r+1,c]

def topple(loc, direction, binary_board):
	h = remove_from_standing(loc)
	[r,c] = loc
	if direction == 0:[sr,sc, er,ec] = [r, c-h,r, c-1]
	elif direction == 1: [sr,sc,er,ec] = [r,c+1,r,c+h]
	elif direction == 2: [sr,sc,er,ec] = [r-h, c, r-1, c]
	elif direction == 3: [sr,sc,er,ec] = [r+1, c, r+h, c]
	game['toppled_crates'].append([sr,sc,er,ec])
	binary_board[r,c] = 0
	for row in range(sr,er+1):
		for col in range(sc, ec+1):
			binary_board[row,col] = 1

def remove_from_standing(loc):
	for cr in game['standing_crates']:
		if [cr[0], cr[1]] == loc:
			[r,c,h] = cr
	game['standing_crates'].remove([r,c,h])
	return h

def can_move(location, direction, bb):
	[rows,cols] = game['board']
	standing = isStanding(location)
	if direction == 0: #left
		if standing and (c - h) >= 0:
			return True
		elif not standing and isAvailable(bb, [location[0], location[1] -1]):
			return True
	if direction == 1: #right
		if standing and c +h < cols:
			return True
		elif not standing and isAvailable(bb,[location[0], location[1]+1]):
			return True
	if direction == 2: #up
		if standing and r-h >=0:
			return True
		elif not standing and isAvailable(bb,[location[0]-1, location[1]]):
			return True	
	if direction == 3: #down
		if standing and r+h < rows:
			return True
		elif not standing and isAvailable(bb,[location[0]+1, location[1]]):
			return True	
	return False

def isAvailable(bb,location):
	print location
	return bb[location[0], location[1]] == 0.0
	

def isStanding(loc):
	for cr in game['standing_crates']:
		if [cr[0], cr[1]] == loc:
			return True
	return False



def find_winners(er,ec):
	wins = [[er-1, ec], [er+1, ec], [er, ec-1], [er, ec+1]]
	final = [sq for sq in wins if not(sq[0] < 0 or sq[0] >= rows or sq[1]<0 or sq[1]>=cols)]
	return final 
	
if __name__ == "__main__":
	fn = 'sample_game'
	game = json.loads(open(fn, 'r').read())
	board = np.zeros(game['board'])
	for cr in game['standing_crates']:
		[r,c,h] = cr
		board[r,c] = h

	start = game['start']
	solve_game(game, start, board)
