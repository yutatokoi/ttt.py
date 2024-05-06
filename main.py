board = [["", "", ""], 
         ["", "", ""], 
         ["", "", ""]]

ROWS = len(board)
COLS = len(board[0])

def place(board, row, col, piece):
    if board[row][col]:
        return board
    else:
        board[row][col] = piece
        return board


def winner(board):
    """ Given a board, if a winner exists, return the piece of the winner.
    Otherwise return None.
    """

    # Check for horizontal wins
    for row in range(ROWS):
        if board[row][0] and board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # Check for vertical wins
    column0 = []
    column1 = []
    column2 = []
    for row in range(ROWS):
        for col in range(COLS):
            if col == 0:
                column0.append(board[row][col])
            if col == 1:
                column1.append(board[row][col])
            if col == 2:
                column2.append(board[row][col])

    if column0 and column0[0] == column0[1] == column0[2]:
        return column0[0]
    if column1 and column1[0] == column1[1] == column1[2]:
        return column1[0]
    if column2 and column2[0] == column2[1] == column2[2]:
        return column2[0]

    # Check for diagonal wins
    if board[1][1]:
        if board[1][1] == board[0][0] == board[2][2]:
            return board[1][1]
        if board[1][1] == board[2][0] == board[0][2]:
            return board[1][1]

    # No winners
    return None


def full(board):
    """ Given a board, return True if full, else False.
    """
    for row in range(ROWS):
        for col in range(COLS):
            if not board[row][col]:
                return False
    return True


def display(board):
    """ Given a board, returns the string representation of the board
    """
    output = "\n"
    for row in range(ROWS):
        for col in range(COLS):
            if not board[row][col]:
                piece = " "
            else:
                piece = board[row][col]

            if col < 2:
                output = output + piece + "|"
            else:
                output = output + piece + "\n"
        if row < 2:
            output += "-----\n"

    return output


def reach(pos1, pos2):
    """ Given two positions (row, col), calculates the third on the board to make
    a line out of the three positions.
    """
    if pos1[0] == pos2[0]:
        return (pos1[0], 3 - (pos1[1] + pos2[1]))
    elif pos1[1] == pos2[1]:
        return (3 - (pos1[0] + pos2[0]), pos1[1])
    else:
        # Diagonal incomplete ATM
        return (1, 1)


def reachExists(board, piece):
    """ Given a board, returns Boolean on whether there is a reach for the given player
    """
    # Incomplete
    return False
    

def main():
    """ 
    1. Bot will always play O. Player will always play X
    """
    
    # Determine if the player or bot will start
    starter = input("Would you like to be the first player (Y or N): ")
    while True:
        try:
            assert(starter == "Y" or starter == "N")
            break
        except Exception:
            starter = input("Would you like to be the first player (Y or N): ")

    if starter == "N":
        place(board, 1, 1, "O")
        display(board)

    # Loop game state while the game can continue
    while not winner(board) and not full(board):
        print(display(board))
        row = int(input("Choose row to place in: "))
        col = int(input("Choose column to place in: "))
        
        place(board, row, col, 'X')
    
    # Declare the winner, or declare the board full
    if winner(board):
        print(display(board))
        print(f'The winner is: {winner(board)} 🎉')
    elif full(board):
        print(display(board))
        print("Board is full. No winners.")
    
    return None


main()


