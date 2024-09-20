def is_solved(board):
        for value in [1, 2]:
            if any(all(cell == value for cell in row) for row in board):
                return value
            if any(all(board[row][col] == value for row in range(3)) for col in range(3)):
                return value
            if all(board[i][i] == value for i in range(3)) or all(board[i][2-i] == value for i in range(3)):
                return value
        if any(board[row][col] == 0 for row in range(3) for col in range(3)):
            return -1
        return 0
        
        
    
board = [
    [1, 2, 2],
    [2, 0, 1],
    [1, 1, 2]
]


result = is_solved(board)
print(result) 
