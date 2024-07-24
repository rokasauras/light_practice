def is_solved(board):
    
    for value in [1, 2]:
        if any(all(cell == value for cell in row) for row in board):
            return value
        if any(all(board[row][col] == value for row in range(3)) for col in range(3)):
            return value
        if any(all(board)):
            return
        
        
        
#
    

    
print(is_solved([[2, 0, 2],
                 [2, 1, 1],
                 [2, 1, 0]]))
