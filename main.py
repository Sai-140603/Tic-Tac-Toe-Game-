# creating the game display
def game_display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
# rows represent the 3 by 3 box in the tic-tac-toe game
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
board = [row1, row2, row3]

def row_selection ():
    row_position=10
    # row position should be in 1,2 or 3
    while row_position not in range(1, 4):
        row_position=int(input("select the row you like :"))

        # if row position is out of range the loop continues until the proper input
        if row_position not in range(1, 4):
            print("select the position like 1,2 or 3")
    return row_position

def column_selection():
    row_pos=row_selection()  # calling the row_selection function to access the row_position value
    col_position = 10
    while col_position not in range(1, 4):
        col_position = int(input("select the col you like :"))
    return row_pos,col_position

current_marker = 'X'

for turn in range(9):  # maximum 9 moves in tic-tac-toe
    print(f"Turn {turn + 1}: Player {current_marker}")

    row, col = column_selection()

    # Check if cell is empty before placing
    if board[row - 1][col - 1] == ' ':
        board[row - 1][col - 1] = current_marker
        game_display(row1, row2, row3)

        # to check the row markers are same to decide the winner
        if (board[0] == [current_marker]*3) or (board[1] ==[current_marker]*3) or (board[2] == [current_marker]*3):
            print(f"BOOYAH!!! {current_marker} Wins ")
            break

        # to check the column markers to decide the winnner
        else:
            winner=False
            for i in range(3):
                if ([board[0][i],board[1][i],board[2][i]])==[current_marker]*3:
                    print(f"BOOYAH!!! {current_marker} Wins ")
                    winner=True
                    break

            if winner==True:
                break


        # add left-to-right diagonal elements
        diag1 = []

        # add right-to-left diagonal elements
        diag2 = []
        for i in range(3):

            # Check left-to-right diagonal
            diag1.append(board[i][i])

            # Check right-to-left diagonal
            diag2.append(board[i][2-i])

        if diag1 == [current_marker] * 3:
            print(f"BOOYAH!!! {current_marker} wins ")
            break

        elif diag2 ==[current_marker] * 3:
            print(f"BOOYAH!!! {current_marker} wins ")
            break


        if current_marker == 'X': # switch the players one after the other
            current_marker="O"
        else:
            current_marker="X"
    else:
        print("Cell already taken. Try again.")
        continue  # repeat the same player's turn

else:
    print("Its a DRAW!!")


game_display(row1,row2,row3)
