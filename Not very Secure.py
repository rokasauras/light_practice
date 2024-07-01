def alphanumeric(password):
    # Check if the 'password' is an instance of the 'str' class and if it is alphanumeric
    if isinstance(password, str) and password.isalnum():
        # If both conditions are true, return True
        return True
    # If either condition is false, return False
    return False

# Test the function
print(alphanumeric("something123"))  # Should return True (all characters are alphanumeric)
print(alphanumeric("something!"))    # Should return False (contains a non-alphanumeric character '!')
print(alphanumeric(12345))           # Should return False (input is not a string)
