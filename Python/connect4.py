winner = False
game_on = True
board = [["0","1","2","3"], 
         [" "," "," "," "], 
         [" "," "," "," "], 
         [" "," "," "," "],
         [" "," "," "," "]]

def display_board(board):
    '''
    Description: 
        Prints the empy game board.
    Arguments: 
        board: A list containing three other lists that represent the rows of a traditional Tic Tac Toe board. 
    Returns: 
        A printed output of the board.
    '''
    print("Here is the current board: ")
    for lst in board[::-1]:
        print(lst)
   
def position_choice():
    '''
    Description: 
        Takes two user inputs that correspond to the indices of the lists and stores them as the row choice and the column choice.
    Arguments: 
        Takes no arguments.
    Returns: 
        row: An integer that will act as the first index that will choose the "row"(list).
        column: An integer that will act as the second index and will choose the position in the list that will be replaced.
    '''
    column_list = [0,1,2,3]
    column = "wrong"
    row = 0
    while column not in column_list and row == 0:
        column = int(input("Pick a column (0-3): "))
        for i in range(0,5):
            if column == i:
                if board[1][i] == " ":
                    row = 1
                
                elif board[2][i] == " ":
                    row = 2
                
                elif board[3][i] == " ":
                    row = 3
                
                elif board[4][i] == " ":
                    row = 4
                
                elif board[4][i] != " ":
                    print("There is no more space in this column. Pick another.")
                    
                return row, column
                              
def replacement_choice(board, row, column):
    '''
    Description: 
        Allows the user to chose a string that will be placed on the board and replaced by the empty " ".
    Arguments:  
        board: The empty list that contains three other lists that have four empty strings in them.
        row: An integer that will act as the first index that will choose the "row"(list).
        column: An integer that will act as the second index and will choose the position in the list that will be replaced.
    Returns:
        board: An updated list of the previos variable 'board'. User's input was put in place of an empty string.
    '''
    pos = "full"
    while pos == "full":
        if board[row][column] == " ":
            user_placement = input("Pick a symbol or string as your character: ") 
            board[row][column] = user_placement
            pos = "empty"
            
        else:
            print("There's already a piece here! Try again.")
            pos = "invalid"
        
        return board
            
def check_winner(board):
    '''
    Description:
        Checks every index to see if there are any 4 in a row horizontally, vertically, or diagonally.
    Arguments:
        board: The empty list that contains three other lists that have four empty strings in them.
    Returns:
        A True or False that'll either keep the game going or exit if there is a winner.
    ''' 
    while winner == False:
        #Checks vertically
        if board[1][0] == board[2][0] and board[2][0] == board[3][0] and board[3][0] == board[4][0] and board[1][0] != " " and board[2][0] != " " and board[3][0] != " " and board[4][0] != " ":
            print("Congrats! You Won.")
            return True
        elif board[1][1] == board[2][1] and board[2][1] == board[3][1] and board[3][1] == board[4][1] and board[1][1] != " " and board[2][1] != " " and board[3][1] != " " and board[4][1] != " " :
            print("Congrats! You Won.")
            return True
        elif board[1][2] == board[2][2] and board[2][2] == board[3][2] and board[3][2] == board[4][2] and board[1][2] != " " and board[2][2] != " " and board[3][2] != " " and board[4][2] != " " :
            print("Congrats! You Won.")
            return True
        elif board[1][3] == board[2][3] and board[2][3] == board[3][3] and board[3][3] == board[4][3] and board[1][3] != " " and board[2][3] != " " and board[3][3] != " " and board[4][3] != " " :
            print("Congrats! You Won.")
            return True
        
        #Checks horizontally
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == board[1][3] and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[1][3] != " ":
            print("Congrats! You Won.")
            return True
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == board[2][3] and board[2][0] != " " and board[2][1] != " " and board[2][2] != " " and board[2][3] != " " :
            print("Congrats! You Won.")
            return True
        elif board[1][0] == board[1][1] and board[3][1] == board[3][2] and board[3][2] == board[3][3] and board[3][0] != " " and board[3][1] != " " and board[3][2] != " " and board[3][3] != " " :
            print("Congrats! You Won.")
            return True
        elif board[1][0] == board[1][1] and board[4][1] == board[4][2] and board[4][2] == board[4][3] and board[4][0] != " " and board[4][1] != " " and board[4][2] != " " and board[4][3] != " " :
            print("Congrats! You Won.")
            return True
        
        #Checks diagonally
        elif board[1][0] == board[2][1] and board[2][1] == board[3][2] and board[3][2] == board[4][3] and board[1][0] != " " and board[2][1] != " " and board[3][2] != " " and board[4][3] != " " :
            print("Congrats! You Won.")
            return True
        elif board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[3][1] == board[4][0] and board[1][3] != " " and board[2][2] != " " and board[3][1] != " " and board[4][0] != " " :
            print("Congrats! You Won.")
            return True

        else:
            return False
                 
if __name__ == "__main__":
    while winner == False:
        display_board(board)
        row,column = position_choice()
        board = replacement_choice(board,row,column)
        winner = check_winner(board)
        if winner == True:
            display_board(board)
        
 