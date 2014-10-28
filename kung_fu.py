import simplejson as json

# 0: Left
# 1: Right
# 2: Up
# 3: Down

def load_game(fn):
	game = json.loads(open(fn, 'r').read())
	"""	
	print type(game['board'])
	print type( game['end'])
	print type(game['start'])
	print type(game['standing_crates'])
	print type(game['toppled_crates'])
	"""
	return game

def solve_game(game):
	[er,ec] = game['end']
	wins = find_winners(er,ec)
	sc = game['standing_crates']
	for crate in [sc[0]]:
		for direction in range(2):
			which_if_toppled(crate,direction) 

def which_if_toppled(box, direction):
	[r,c,h] = box
	new_sqs = -1
	if direction == 0:
		if (c - h -1) >= 0:
			new_sqs = [[r,j] for j in range(c-1,c-h-1, -1)]
	if direction == 1:
		if c +1 +h < cols:
			new_sqs = [[r,j] for j in range(c+1, c+1+h)]
	if direction == 2:
		if r-1-h >=0:
			new_sqs = [[i,c] for i in range(r-1,r-1-h,-1)]
	if direction == 3:
		if r+1+h < rows:
			new_sqs = [ [i,c] for i in range(r+1, r+1+h)]

def find_winners(er,ec):
	wins = [[er-1, ec], [er+1, ec], [er, ec-1], [er, ec+1]]
	final = [sq for sq in wins if not(sq[0] < 0 or sq[0] >= rows or sq[1]<0 or sq[1]>=cols)]
	return final 
	
if __name__ == "__main__":
	fn = 'sample_game'
	game = load_game(fn)
	[rows,cols] = game['board']
	solve_game(game)
