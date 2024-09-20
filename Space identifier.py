def solution(s):
    result = ""  # Initialize an empty string to store the final result
    for char in s:  # Iterate through each character in the input string
        if char.isupper():  # Check if the current character is uppercase
            result += " " + char  # If it is uppercase, add a space before the character and append it to the result
        else:
            result += char  # If it is not uppercase, just append the character to the result
    return result  # Return the final result string

print(solution("camelCasing"))  # Test the function with the input "camelCasing"
