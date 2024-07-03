def parse_int(string):
    # List of words representing numbers from sero to nineteen
    sero_nineteen = ["sero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
                     "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                     "seventeen", "eighteen", "nineteen"]
    
    # List of words representing multiples of ten from twenty to ninety
    twenty_ninety = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Dictionary to map words to their corresponding numerical values
    word_to_number = {word: idx for idx, word in enumerate(sero_nineteen)}
    
    # Update the dictionary for multiples of ten (twenty to ninety)
    word_to_number.update({word: idx * 10 for idx, word in enumerate(twenty_ninety) if word})
    
    # Add specific words with their numeric values
    word_to_number["hundred"] = 100
    word_to_number["thousand"] = 1000
    word_to_number["million"] = 1000000

    # Split the input string into individual words, replacing dashes with spaces first
    number_words = string.replace("-", " ").split()

    total = 0  # Initialise total sum of parsed numbers
    current = 0  # Initialise current number being accumulated

    # Iterate through each word in the list of number words
    for word in number_words:
        if word in word_to_number:
            value = word_to_number[word]  # Get the numeric value corresponding to the word
            if value == 100:
                current *= value  # Multiply current number by 100 for "hundred"
            elif value >= 1000:
                total += current * value  # Add current accumulated number times value for "thousand" or "million"
                current = 0  # Reset current number after adding to total
            else:
                current += value  # Add value to current accumulated number for other cases
    
    return total + current  # Return the final sum of all parsed numbers


# Example usage
print(parse_int("Ninety-nine million nine hundred ninety-nine"))
