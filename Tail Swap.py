def tail_swap(strings):
    # Split each string in the list at the colon and store the parts in a new list
    parts = [s.split(':') for s in strings]
    
    # Create new strings by swapping the parts after the colon
    # parts[0][0] is the part before the colon in the first string ("abc")
    # parts[1][1] is the part after the colon in the second string ("456")
    # parts[1][0] is the part before the colon in the second string ("cde")
    # parts[0][1] is the part after the colon in the first string ("123")
    swapped_strings = [
        parts[0][0] + ':' + parts[1][1],  # First part of first string + ":" + second part of second string ("abc:456")
        parts[1][0] + ':' + parts[0][1]   # First part of second string + ":" + second part of first string ("cde:123")
    ]
    
    # Return the list of swapped strings
    return swapped_strings

# Test the function with example input and print the result
print(tail_swap(["abc:123", "cde:456"]))  # Expected output: ["abc:456", "cde:123"]
