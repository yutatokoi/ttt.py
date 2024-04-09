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
    for row in range(ROWS):
        if board[row][0] and board[row][0] == board[row][1] == board[row][2]:
            return True

def full(board):
    """ Given a board, check if it is full or not. Return boolean.
    """
    for row in range(ROWS):
        for col in range(COLS):
            if not board[row][col]:
                return False
    return True

def main():
    while not winner(board) or full(board):
            

de

