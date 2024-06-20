# Hashtag generator

def generate_hashtag(s):
    # Convert the input to a string
    string = str(s)
    # Get the length of the input string
    Length_of_content = len(string)
    
    # Check if the input string is not empty
    if Length_of_content > 0:
        # Capitalize the first letter of each word and join them with spaces
        string = ' '.join(w.capitalize() for w in s.split()) 
        # Prepend a '#' to the capitalized string
        string = "{} {}".format('#', string)
        # Remove all spaces to form the hashtag
        string = string.replace(" ", "")
        # Capitalize the first letter of the first word after the '#'
        First_Letter = string[1].capitalize()
        # Replace the first letter of the first word with its capitalized form
        string = string.replace(string[1], First_Letter)
        # Get the length of the resulting hashtag
        character_length = len(string)
        
        # Check if the resulting hashtag is too long
        if character_length > 140:
            return False
        # Check if the resulting hashtag is just '#' or empty
        if string == "#" or len(string) == 1:
            return False
        else:
            # Return the valid hashtag
            return string
    else:
        # Return False if the input string is empty
        return False

# Test the hashtag generator function with a sample input
print(generate_hashtag("c i n"))
