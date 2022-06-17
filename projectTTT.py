from random import randrange

print ("Welcome to the game. You have 20 spaces.")
print ("You are playing with X, computer with O.")
print ("The one who places three of their own marks next to each other wins.")
board = "--------------------"
question = ("Choose the number 1-20 that corresponds to a space where you want to your mark: ")

def player_move (board):
    while True:
        position_1 = int(input(question))
        if position_1 < 1:
            print ("Small number. Try again")     
        elif position_1 > 20:
            print ("Number if too big. Try again")
        elif board[position_1-1] == "X":
            print ("Slot is taken")
        elif board[position_1-1] == "O":
            print ("Slot is taken")
        else:
            board_player=board[:position_1-1]+"X"+board[position_1:]
            board = board_player
            print ("Your move:",board)
            return board

def pc_move (board):
    while True:
        position_pc = randrange (1,21)
        if board[position_pc] == "X":
            position_pc = randrange (1,21)
        elif board[position_pc] == "O":
            position_pc = randrange (1,21)
        elif board[position_pc] == "-":
            board_pc = board[:position_pc-1]+"O"+board[position_pc:]
            board = board_pc
            print ("PC move:",board)
            return board


def evaluation (board):
    player_winning_comb = "XXX"
    comp_winning_comb = "OOO"
    if player_winning_comb in board:
        print ("You won!")
    elif comp_winning_comb in board:
        print ("Computer won!")
    elif not "-" in board:
        print ("Draw. Maybe one more game?")
    else:
        print ("Continue playing")

player_winning_comb = "XXX"
comp_winning_comb = "OOO"
while True:
    board = player_move(board)
    if player_winning_comb in board:
        print ("You won!", board)
        break
    elif comp_winning_comb in board:
        print ("Computer won!", board)
        break
    elif not "-" in board:
        print ("Draw. Maybe one more game?", board)
        break
    
    board = pc_move(board)
    if player_winning_comb in board:
        print ("You won!")
        break
    elif comp_winning_comb in board:
        print ("Computer won!")
        break
    elif not "-" in board:
        print ("Draw. Maybe one more game?")
        break

