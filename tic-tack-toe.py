def is_solved(board):
    """
    Determines the state of a Tic-Tac-Toe board.

    Parameters:
    board (list of list of int): A 3x3 board where each cell contains 0 (empty), 1, or 2.

    Returns:
    int: 1 if player 1 has won, 2 if player 2 has won, -1 if the game is not finished (empty cells), 0 if it's a draw.
    """
    
    # Check if player 1 or player 2 has won
    for value in [1, 2]:
        # Check if any row is completely filled with the current player's value
        if any(all(cell == value for cell in row) for row in board):
            return value
        
        # Check if any column is completely filled with the current player's value
        if any(all(board[row][col] == value for row in range(3)) for col in range(3)):
            return value
        
        # Check if the main diagonal (top-left to bottom-right) is completely filled with the current player's value
        if all(board[i][i] == value for i in range(3)):
            return value
        
        # Check if the anti-diagonal (top-right to bottom-left) is completely filled with the current player's value
        if all(board[i][2 - i] == value for i in range(3)):
            return value
    
    # Check if there are any empty cells (value 0) on the board
    if any(board[row][col] == 0 for row in range(3) for col in range(3)):
        return -1  # Game is not finished yet
    
    # If no winner and no empty cells, it’s a draw
    return 0

# Example board configuration
board = [
    [1, 2, 2],
    [2, 0, 1],
    [1, 1, 2]
]

# Determine the game result
result = is_solved(board)
print(result)  # Expected output: -1 (since there is still an empty cell)
