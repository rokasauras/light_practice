def rgb(r, g, b):
    def to_hex(value):
        # Ensure the value is within the range 0-255
        value = max(0, min(value, 255))
        # Convert the integer part to a hexadecimal string
        digit1 = value // 16
        # Convert the remainder to a hexadecimal string
        digit2 = value % 16
        # Convert both to hexadecimal characters and combine them
        return f'{digit1:X}{digit2:X}'

    # Combine all three parts
    return to_hex(r) + to_hex(g) + to_hex(b)

print(rgb(255, 255, 255))  # Output: FFFFFF
