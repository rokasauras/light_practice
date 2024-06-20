'''
Sort through each letter or number, ensuring there are no consecutive duplicates.

This may involve taking the first character and only printing it if the character before it is not the same.
'''

def unique_in_order(sequence):
    # Check if the sequence is empty. If so, return an empty list.
    if not sequence:
        return []

    # Initialize a list to store unique elements.
    result = [sequence[0]]

    # Iterate through the sequence starting from the second element.
    for item in sequence[1:]:
        # Check if the current item is different from the last item added to result.
        # If different, append it to the result list.
        if item != result[-1]:
            result.append(item)

    # Return the list of unique elements.
    return result

# Example usage:
print(unique_in_order('somMetthiiiing123'))  # Output: ['s', 'o', 'm', 'M', 'e', 't', 'h', 'i', 'n', 'g', '1', '2', '3']
