def alphabet_position(text):
    # Convert the input text to a string (in case it's not already a string)
    text_string = str(text)
    
    # Initialize an empty list to store the positions of alphabetic characters
    index_list = []
    
    # Iterate over each character in the input string
    for letters in text_string:
        # Check if the character is an alphabetic letter
        if letters.isalpha():
            # Convert the letter to lowercase and find its position in the alphabet
            # 'a' is 1, 'b' is 2, ..., 'z' is 26
            position = ord(letters.lower()) - ord('a') + 1
            # Append the position to the list
            index_list.append(position)
    
    # Join the list of positions into a single string, with each position separated by a space
    index_string = ' '.join(str(i) for i in index_list)
    
    # Return the resulting string of positions
    return index_string

# Test the function with a sample input and print the result
print(alphabet_position("The sunset sets at twelve o' clock."))
