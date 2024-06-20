def high_and_low(numbers):
    # Convert the input string of numbers into a list of integers
    data = list(map(int, numbers.split()))  # Splits the string by spaces and converts each part to an integer
    
    # Find the minimum value in the list
    min_value = min(data)  # Finds the smallest integer in the list
    
    # Return the minimum value
    return min_value

# Example usage:
print(high_and_low("1 2 3 4 5"))  # Output: 1 (Returns the smallest number in the input string)
