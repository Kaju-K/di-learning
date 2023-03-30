import os
import time

positions = [' ' for _ in range(9)]
player = "X"
winning_positions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

x_indexes = set()
o_indexes = set()

def position_board():
    numbers = [str(i) for i in range(9)]
    numbers_matrix_board = [numbers[i*3:(i+1)*3] for i in range(3)]
    for row in numbers_matrix_board:
        print(" | ".join(row))

def create_board():
    matrix_board = [positions[i*3:(i+1)*3] for i in range(3)]
    return matrix_board

def print_board():
    for row in create_board():
        print(" | ".join(row))

def change_player():
    global player
    if (player == "X"):
        player = "O"
    else:
        player = "X"

def player_move(move):
    if (move.lower() == "positions"):
        position_board()
    else:
        try:
            num_move = int(move)
            if (0 <= num_move <= 8):
                if positions[num_move] == " ":
                    positions[num_move] = player
                    if player == "X":
                        x_indexes.add(num_move)
                    else:
                        o_indexes.add(num_move)
                    if not(check_winner()):
                        change_player()
                    return True
                else:
                    print("This space is occupied. Try again. If you need to see the board with positions again, type: positions")
            else:
                print("You should put a number between 0 and 8 as a move. Try again. If you need to see the board with positions again, type: positions")
        except:
            print("You need to put a number as a move. Try again. If you need to see the board with positions again, type: positions")

def check_winner():
    for win in winning_positions:
        if (set(win).issubset(x_indexes)) or (set(win).issubset(o_indexes)):
            return True

def playing():
    os.system("cls")
    position_board()
    round = 0
    while True:
        time.sleep(0.5)
        if not(round):
            round += 1
        else:
            os.system("cls")
            print_board()
        print(f"It's the turn of the \"{player}\" player.")
        while True:
            move = input("Choose a number between 0-8: ")
            if (player_move(move)):
                break
        if check_winner():
            os.system("cls")
            print_board()
            print(f"Congratulations! {player} won!")
            break
        if (x_indexes.union(o_indexes) == set([i for i in range(9)])):
            os.system("cls")
            print_board()
            print("It's a draw!")
            break
    
playing()