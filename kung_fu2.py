import simplejson as json
import numpy as np
import copy
# 0: Left
# 1: Right
# 2: Up
# 3: Down

#type(game['board'])
#type( game['end'])
#type(game['start'])
#type(game['standing_crates'])
#type(game['toppled_crates'])
dir_map = {0:'left', 1:'right', 2:'up', 3:'down'}

def solve_game(location, current_board, visited):
	visited[location] =1
	print location
	print current_board
	print '------------------'
	if location == game['end']:
		print "made it home"
		return True
	standing = isStanding(location, current_board)
	for direction in range(4):
		"""
		if standing:
			print 'going to fall '+ dir_map[direction]
			if canFall(location, current_board, direction):
				[current_board, location] =topple(location, current_board, direction)
			else:
				return False
		else:
			#print canMove(location, current_board, direction, visited) #CHECK TO SEE IF IT WASN'T already visitedi
			print 'not on a standing sq'
			if canMove(location, current_board, direction, visited):
				location = moveOne(location, current_board, direction)
				print 'going to move' + dir_map[direction]
			else:
				return False
		
		solve_game(location, current_board, visited)"""
		return moveLeft or moveRight or moveUp or moveDown

#check to see if the current location is standing
def isStanding(location, current_board):
	[r,c] = location
	return current_board[r,c] > 1


#Check to see if this location can fall in the desired direction
def canFall(location, current_board, direction):
	if not isStanding(location, current_board): return False
	[r,c] = location
	h = current_board[r,c]
	[rows, cols] = current_board.shape
	if direction == 0:
		if c-h < 0: 
			return False
		return sum(current_board[r,(c-h):c]) == 0
	elif direction == 1:
		if c+h >= cols:
			return False
		return sum(current_board[r, (c+1):(c+h+1)]) == 0
	elif direction == 2:
		if r-h < 0: return False
		return sum(current_board[r-h:r, c]) == 0
	elif direction == 3:
		if r+h >= rows: return False
		return sum(current_board[r+1:r+h+1,c])==0

#ONLY FOR NOT STANDING LOCATIONS
#CAN I MOVE IN THE DESIRED DIRECTION 
def canMove(location, current_board, direction, visited):
	[r,c] = location
	try:
		if direction == 0: return current_board[r,c-1] != 0 and not visited[r,c-1]
		elif direction == 1: return current_board[r,c+1] !=0 and not visited[r,c+1]
		elif direction == 2: return current_board[r-1,c] !=0 and not visited[r-1,c]
		elif direction == 3: return current_board[r+1,c] !=0 and not visited[r+1,c]
	except IndexError:
		return False

def moveOne(location, current_board, direction):
	[r,c] = location
	if direction == 0: location = [r,c-1]
	elif direction == 1:location=[r,c+1] 
	elif direction == 2:location= [r-1,c]
	elif direction == 3:location = [r+1,c]
	return location


#knock the standing crates over in the desired direction
#AND update the board!
def topple(location, current_board, direction):
	[r,c] = location
	h = current_board[r,c]
	new_board = copy.deepcopy(current_board)
	new_board[r,c] = 0
	if direction == 0:
		new_board[r,c-h:c] = 1
		new_location = [r,c-1]
	elif direction == 1:
		new_board[r,c+1:c+h+1] = 1
		new_location = [r,c+1]
	elif direction == 2:
		new_board[r-h:r, c] = 1
		new_location = [r-1,c]
	elif direction == 3:
		new_board[r+1:r+h+1, c] = 1
		new_location = [r+1,c]
	return [new_board, new_location]


	

if __name__ == "__main__":
	fn = 'sample_game'
	game = json.loads(open(fn, 'r').read())
	board = np.zeros(game['board'])
	visited = np.zeros(game['board'])
	for cr in game['standing_crates']:
		[r,c,h] = cr
		board[r,c] = h
#	print board
#	start = game['start']
#	solve_game(start, board,visited)

