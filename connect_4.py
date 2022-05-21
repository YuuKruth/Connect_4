from tokenize import String
import numpy as np

#TODO: fix Hardcode; custom size of board but it have to be at least 6 rows and 7 columns big; this fix is effecting to other todo  
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #matrix filled with 0; 6 colums 7 rows
    return board

def drop_piece(board , row, col, piece):
    board[row][col] = piece

#checks the typed numer of player is valid
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0 #TODO: fix Hardcode

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#changes the orientation of the array
def print_board(bord):
    print(np.flip(board, 0))

#TODO: fix magic numbers / hardcode (later)
#TODO: build more efficient winning_check algorithm!!
def winning_check(board, piece):

    #this is a temporary algorithm for testing
    #check horizontal locations for win
    for c in range(COLUMN_COUNT - 3): # - 3 cause you can only win with 4 pieces in column to the left and right
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    #check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3): # - 3 cause you can only win with 4 pieces in row to the top and bottom
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True            

    #check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3): 
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True 

    #check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT): 
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

#Play_algorithm

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask Player 1 to input
    if turn == 0:

        col = 0
        while True:
            col_test = int(input("Player 2 Make your selection (0-" + str(COLUMN_COUNT - 1) + "): "), 10)

            if col_test == range(COLUMN_COUNT):
                col = int(col_test)
                break
                
            else:
                print("ERROR INPUT -> Input has to be between 0 and " + str(COLUMN_COUNT - 1)))
                print("please try again:") 


        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_check(board, 1):
                print("PLAYER 1 Wins!")
                game_over = True

         

    # Ask Player 2 to input
    else:
        try: #exit loop if player types nothing
            col = int(input("Player 2 Make your selection (0-" + str(COLUMN_COUNT - 1) + "): "), 10)
            
            if col != range(COLUMN_COUNT):
                print("ERROR INPUT -> Input has to be between 0 and " + str(COLUMN_COUNT - 1))
                break
        
        except ValueError:
            print("ERROR INPUT -> Input has to be a number between 0 and " + str(COLUMN_COUNT - 1))
            break


        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_check(board, 2):
                print("PLAYER 2 Wins!")    
                game_over = True

         


    print_board(board)        

    turn += 1
    turn = turn % 2