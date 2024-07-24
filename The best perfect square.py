def find_next_square(sq):
    perfect_square = sq**0.5
    if perfect_square.is_integer():
        perfect_square += 1
        return(perfect_square**2)
    else:
        perfect_square = int(perfect_square) + 1
        return(perfect_square**2)
    
print(find_next_square(1234))
    

# Return the next square if sq is a square, -1 otherwise

