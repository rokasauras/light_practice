def binary_array_to_number(arr):
    # Join elements of the array into a single string of binary digits,
    # convert each element to string first using map and str functions,
    # then join them together into one string.
    binary_string = "".join(map(str, arr))
    
    # Convert the binary string to a decimal (base-10) integer using Python's int function,
    # specifying base 2 since the input is in binary format.
    decimal_number = int(binary_string, 2)
    
    # Return the resulting decimal number.
    return decimal_number

# Example usage:
print(binary_array_to_number([0,1,0,1]))  # Outputs: 5






