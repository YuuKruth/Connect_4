import numpy as np
import pygame as pg
import sys

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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            #pygame.draw.rect(Surface, color, Rect, width = 0)
            pg.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            #pygame.draw.circle(Surface, color, pos, radius, width = 0)
            pg.draw.circle(screen, BLACK, (c * SQUARESIZE + RADIUS, r * SQUARESIZE + SQUARESIZE + RADIUS), RADIUS - 5)

#Play_algorithm
board = create_board()
print_board(board)
game_over = False
turn = 0

#pygame
 #pygame window
pg.init()
pg.display.set_caption('CONNECT 4 GAME')
Icon = pg.image.load('connect_4_icon.png')
pg.display.set_icon(Icon)

 #pygame board 
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE + SQUARESIZE

size = (width, height)
screen = pg.display.set_mode(size)

 #Rectangular
BLUE = (30, 144, 255)

 #Circle
BLACK = (0, 0, 0)
RADIUS = int(SQUARESIZE/2) #RADIUS-5 for no merging circles



draw_board(board)
pg.display.update()

while not game_over:
    #pygame
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN: 
            continue 
            # Ask Player 1 to input
            # if turn == 0:
            #     #making sure that all inputs are correct
            #     while True:
            
            #         try:
            #             col_test = int(input("Player 1 Make your selection (0-" + str(COLUMN_COUNT - 1) + "): "), 10)
                
            #             if 0 <= col_test and col_test < COLUMN_COUNT:
                    
            #                 col = int(col_test)
            #                 break
                
            #             else:
            #                 print("ERROR INPUT -> Input has to be between 0 and " + str(COLUMN_COUNT - 1))
            #                 print("please try again:")

            #         except ValueError:
            #             print("ValueError  --> Input has to be numeric! (positive integer)")
            #             print("ERROR INPUT --> Input has to be between 0 and " + str(COLUMN_COUNT - 1))
            #             print("please try again:")
            #             pass


            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 1)

            #         if winning_check(board, 1):
            #             print("PLAYER 1 Wins!")
            #             game_over = True

         

            # # Ask Player 2 to input
            # else:

            #     #making sure that all inputs are correct
            #     while True:
            
            #         try:
            #             col_test = int(input("Player 2 Make your selection (0-" + str(COLUMN_COUNT - 1) + "): "), 10)

            #             if 0 <= col_test and col_test < COLUMN_COUNT:
            #                 col = int(col_test)
            #                 false_input_count = 0
            #                 break
                
            #             else:
            #                 print("ERROR INPUT -> Input has to be between 0 and " + str(COLUMN_COUNT - 1))
            #                 print("please try again:")

            #         except ValueError:
            #             print("ValueError")
            #             print("ERROR INPUT -> Input has to be between 0 and " + str(COLUMN_COUNT - 1))
            #             print("please try again:")
            #             pass


            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 2)

            #         if winning_check(board, 2):
            #             print("PLAYER 2 Wins!")    
            #             game_over = True

            # print_board(board)        

            # turn += 1
            # turn = turn % 2