from random import randrange

print ("Welcome to the game. You have 20 spaces. \nYou are playing with X, computer with O. \nThe one who places three of their own marks next to each other wins.")
board = "--------------------"
question = ("Choose the number 1-20 that corresponds to a space where you want to your mark: ")

def player_move (board, mark):
    position_1 = int(input(question))
    while True:
        if position_1 < 1:
            print ("Small number. Try again")
            position_1 = (int(input(question)))     
        elif position_1 > 20:
            print ("Number if too big. Try again")
            position_1 = (int(input(question)))
        elif board[position_1-1] == "X":
            print ("Slot is taken")
            position_1 = (int(input(question)))
        elif board[position_1-1] == "O":
            print ("Slot is taken")
            position_1 = (int(input(question)))
        else:
            board_move = board[:position_1-1]+mark+board[position_1:]
            break
    return board_move


def pc_move (board):
    position_pc = randrange (1,20)
    while True:
        if board[position_pc] == "X":
            position_pc = randrange (1,20)
        elif board[position_pc] == "O":
            position_pc = randrange (1,20)
        elif board[position_pc] == "-":
            board = board[:position_pc-1]+"O"+board[position_pc:]
            break
    return board

def evaluation ():
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

while True:
    #print (player_move(board, "X"))
    print (pc_move(print(player_move(board, "X"))))