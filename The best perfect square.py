def find_next_square(sq):
    # Calculate the square root of sq
    perfect_square = sq**0.5
    
    # Check if the square root is an integer (i.e., sq is a perfect square)
    if perfect_square.is_integer():
        # If sq is a perfect square, increment the square root by 1
        perfect_square += 1
        
        # Return the square of the incremented value (next perfect square)
        return int(perfect_square**2)
    else:
        # If sq is not a perfect square, find the next integer greater than the square root
        perfect_square = int(perfect_square) + 1
        
        # Return the square of this next integer (next perfect square)
        return int(perfect_square**2)
    
# Example usage:
print(find_next_square(1234))  # Output: 1296 (36^2)

# Return the next square if sq is a square, -1 otherwise
