'''
Sort through each letter or number, ensuring there are no consecutive duplicates.

This may involve taking the first character and only printing it if the character before it is not the same.

'''

def unique_in_order(sequence):
    if not sequence:
        return []
    result = [sequence[0]]

    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)

    return result

print(unique_in_order('somMetthiiiing123'))

