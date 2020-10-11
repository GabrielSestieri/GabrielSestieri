game_on = True
game_list = [0,1,2]
board = [[" "," "," "," "],
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
    print(board)
    
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
    row = "wrong"
    column = "wrong"
    while row and column not in game_list:
        row = int(input("Pick a row (0-3): "))
        column = int(input("Pick a column (0-3): "))
        
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
    user_placement = input("Pick a symbol or string as your character: ")
    board[row][column] = user_placement
    return board

def gameon_choice():
    '''
    Description:
        Gives the user the option to exit the game or carry on.
    Arguments:
        Takes no arguments.
    Returns:
        Either True or False.
    '''
    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Keep playing? (Y/N): ")
        
        if choice not in ["Y", "N"]:
            print("Sorry I don't understnad")
    if choice == "Y":
        return True
    else:
        return False
    

if __name__ == "__main__":
    while game_on == True:
        display_board(board)
        row,column = position_choice()
        board = replacement_choice(board, row,column)
        display_board(board)
        game_on = gameon_choice()
        display_board()