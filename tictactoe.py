import string

size = 5 #max 10
Map = [[' ' for x in range(size)] for y in range(size)] 


def cls():
	print('\x1b[2J')

def drawMap(x):
	turn = ''
	if (x%2 == 0):
		turn = 'X'
	else:
		turn = 'O'
	print("Game Round: " + str(x), end ="\n")
	print("Current Move: " + turn, end ="\n")
	print('\033[4m', end = '')
	for row in range(size+1):
		if row == 0:
			print(" |", end ='')
		else:
			print(string.digits[row-1] + '|', end ='')
		for col in range(size):
			if row == 0:
				print(string.ascii_lowercase[col], end ='|')
			else:
				print(Map[row-1][col], end ='|')

			if col == size-1:
				print('')
	print('\033[0m', end = '')

def checkEmpty(x):
	if (x == ' '):
		return True
	else:
		return False

def checkWin(x, y, gameRound):
	if (gameRound%2 == 0):
		s = 'X'
	else:
		s = 'O'

	#columns
	for i in range(0, size):
		if(Map[x][i] != s):
			break
		if(i == size-1):
			return s
	
	#rows
	for i in range(0, size):
		if(Map[i][y] != s):
			break
		if(i == size-1):
			return s

	#diag
	if(x == y):
		for i in range(0, size):
			if(Map[i][i] != s):
				break
			if(i == size-1):
				return s

	#antidiag
	if(x + y == size - 1):
		for i in range(0, size):
			if(Map[i][(size-1)-i] != s):
				break
			if(i == size-1):
				return s

	#check draw
	if(gameRound == (size*size - 1)):
		return "tie"
		
		


def Game():
	cls()
	gameRound = 0
	end = False
	while not end:
		cls()
		drawMap(gameRound)
		while True:
			Move = input()
			if (Move == 'x'):
				end = True
				break
			if (len(Move) == 2 and Move[0].isnumeric() and Move[1].islower()):
				row = int(Move[0])
				col = string.ascii_lowercase.index(Move[1])
				if (row >= 0 and row <= size-1 and col >= 0 and col <= size-1):
					if (checkEmpty(Map[row][col]) == True):
						if (gameRound%2 == 0):
							Map[row][col] = 'X'
						else:
							Map[row][col] = 'O'
						if (checkWin(row,col,gameRound) == 'X'):
							cls()
							drawMap(gameRound)
							print("Player X won.")
							end = True
						elif (checkWin(row,col,gameRound) == 'O'):
							cls()
							drawMap(gameRound)
							print("Player O won.")
							end = True
						elif (checkWin(row,col,gameRound) == "tie"):
							cls()
							drawMap(gameRound)
							print("The game was a tie.")
							end = True
						break
					else:
						print("That spot is already occupied.")
				else:
					print("Move needs to be within the board.")

			else:
				print("Incorrect format. Move needs to be a number and character. Like 1a.")
		gameRound +=1
		
Game()

