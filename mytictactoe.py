from termcolor import colored, cprint

def main():
    playerone = input("Player 1, enter your name: ")
    playertwo= input("Player 2, enter your name: ")
    gameboard = new_gameboard()
    winner_text = colored ('winner!!' , 'green' , attrs=['reverse','blink']) 

    while not (winner(gameboard) or isadraw(gameboard)):
        print()
        board_template(gameboard)
        print()
        first_run(playerone, gameboard)
        print()
        board_template(gameboard)
        print()
        second_run(playertwo, gameboard)
        
    board_template(gameboard)
    cprint(f"Congratulations you are the {winner_text}")

def first_run(playerone, board):
    choose = input(f" {playerone.capitalize()} you are playing as \033[2;31;40m  X \033[2;37;40m  , please choose a slot available from 1 to 9: ")
    choose = int(choose)
    if choose <= 9:
        board[choose - 1] = "X" 


def second_run(playertwo, board):
    choose = input(f" {playertwo.capitalize()} you are playing as \033[1;34;40m O \033[1;37;40m , please choose a slot available from 1 to 9: ")
    choose = int(choose)
    if choose <= 9:
        board[choose - 1] = "0" 

def new_gameboard():
    board =[]
    for square in range(9):
        board.append(square + 1)
    return board

def board_template(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + -")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def isadraw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 


def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
            
if __name__ == "__main__":
    main()