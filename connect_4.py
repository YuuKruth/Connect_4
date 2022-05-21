import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #matrix filled with 0; 6 colums 7 rows
    return board

def drop_piece(board , row, col, piece):
    board[row][col] = piece

#checks the typed numer of player is valid
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0 #range mybe change

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#changes the orientation of the array
def print_board(bord):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask Player 1 to input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6): "), 10)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)


    # Ask Player 2 to input
    else:
        col = int(input("Player 2 Make your selection (0-6): "), 10)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)        

    turn += 1
    turn = turn % 2