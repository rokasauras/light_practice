<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1>Python Utility Functions</h1>

  <p>This repository contains multiple Python functions designed to solve distinct problems, listed below:</p>

  <hr>

  <h2>Converting a Binary Array to a Decimal Number - binary_array_decoder</h2>

  <h3>Description</h3>

  <p>This function converts a binary array (series of 0s and 1s) to its corresponding decimal (base-10) value.</p>

  <h3>Features</h3>

  <ul>
    <li>Handles binary arrays of any length.</li>
    <li>Efficiently calculates the decimal value using bitwise operations.</li>
  </ul>

  <hr>

  <h2>Finding the Complementary DNA Strand</h2>

  <h3>Description</h3>

  <p>Automates finding the complementary DNA strand based on base pairing rules:</p>
  <ul>
    <li>A pairs with T</li>
    <li>C pairs with G</li>
  </ul>

  <h3>Features</h3>

  <ul>
    <li>Takes a DNA strand (string) as input.</li>
    <li>Outputs the complementary DNA strand.</li>
    <li>Handles both uppercase and lowercase letters.</li>
  </ul>

  <hr>

  <h2>Paino Tiles Game Bot</h2>

  <h3>Description</h3>

  <p>Automates playing the Paino Tiles game by detecting black pixels at user-specified click locations.</p>

  <h3>Features</h3>

  <ul>
    <li>Allows the user to define click coordinates.</li>
    <li>Analyses the screen for black pixels at those coordinates.</li>
  </ul>

  <hr>

  <h2>No Duplicates Script</h2>

  <h3>Description</h3>

  <p>Ensures a sequence (list or array) contains no duplicate elements by comparing each element to the previous ones.</p>

  <h3>Features</h3>

  <ul>
    <li>Takes a sequence of elements as input.</li>
    <li>Removes any duplicate elements from the sequence.</li>
    <li>Maintains the order of unique elements.</li>
  </ul>

  <hr>

  <h2>Highest and Lowest Numbers</h2>

  <h3>Description</h3>

  <p>The <code>high_and_low</code> function takes a string of numbers separated by spaces and returns the highest and lowest numbers in the sequence.</p>

  <h3>Features</h3>

  <ul>
    <li>Input: Accepts a string of numbers separated by spaces.</li>
    <li>Output: Returns a string containing the highest and lowest numbers separated by a space.</li>
    <li>Error Handling: Assumes valid input format (numbers separated by spaces).</li>
    <li>Efficiency: Utilises Python's built-in <code>min()</code> and <code>max()</code> functions for optimal performance.</li>
    <li>String Formatting: Uses Python's f-string for clear and concise output formatting.</li>
  </ul>

  <hr>

  <h2>Hashtag Generator</h2>

  <h3>Description</h3>

  <p>Generates a hashtag from a given string.</p>

  <h3>Features</h3>

  <ul>
    <li>Removes spaces from the input string.</li>
    <li>Capitalises the first letter of each word.</li>
    <li>Ensures non-empty input for hashtag generation.</li>
  </ul>

  <hr>

  <h2>Index Position</h2>

  <h3>Description</h3>

  <p>Converts each alphabetic letter in the input text to its corresponding position in the alphabet.</p>

  <h3>Features</h3>

  <ul>
    <li>Iterates over each character in the string.</li>
    <li>Checks if the character is an alphabetic letter.</li>
    <li>Converts each alphabetic letter to lowercase.</li>
    <li>Computes the position using the ASCII value.</li>
    <li>Returns the list of alphabetic positions.</li>
  </ul>

  <hr>
  
  <h2>Space Identifier</h2>
    
  <h3>Description</h3>
    
  <p>The <code>solution</code> function in Python converts a camelCase formatted string into a spaced format where each uppercase letter (except the first) is preceded by a space.</p>
    
  <h2>Usage</h2>
  <p>Call <code>solution(s)</code> where <code>s</code> is the camelCase string you want to convert. It returns the converted string.</p>
    
  <h2>Example</h2>
  <pre><code>
  print(solution("camelCasing"))  # Output: "camel Casing"
  </code></pre>
    
  <p>This function is useful for formatting camelCase strings into a more readable format, often used in display or user interface contexts where separation between words is needed.</p>
  
  <hr>
  
  <h2>The perfect square</h2>
    
  <h3>Description</h3>
    
  <p>The <code>find_next_square</code> function calculates and returns the next perfect square greater than a given number <code>sq</code> or returns <code>-1</code> if <code>sq</code> is not a perfect square.</p>
    
  <h3>Features</h3>
  <ul>
    <li>Identifies the next perfect square greater than a given number.</li>
    <li>Returns <code>-1</code> if the input number is not a perfect square.</li>
  </ul>
        
  <p>Example usage:</p>
  <pre><code>
  print(find_next_square(1234))  # Output: 1296 (36^2)
  </code></pre>
    
  <p>This function is handy for scenarios where determining the next perfect square number is required, such as in mathematical computations or algorithms.</p>
  
  <hr>

  <h2>Tail Swap</h2>

  <h3>Description</h3>

  <p>This is a Python function that swaps the parts of two input strings after the colon (<code>:</code>). The function takes a list of two strings as input and returns a list of two strings with the parts after the colon swapped.</p>

  <h3>Features</h3>
  <ul>
    <li>Efficiently swaps the parts after the colon in two strings.</li>
    <li>Utilizes list comprehensions for concise and readable code.</li>
    <li>Demonstrates the use of list indexing and string manipulation in Python.</li>
  </ul>
  <h2>Example</h2>
  <p>Given the input <code>["abc:123", "cde:456"]</code>, the function will return <code>["abc:456", "cde:123"]</code>.</p>

  <hr>

  <h2>RGB to HEX Color Converter</h2>

  <h3>Description</h3>

  <p>This project provides a simple Python function to convert RGB color values to their hexadecimal (HEX) representation. The function ensures the RGB values are within the valid range (0-255) and accurately converts them to a two-digit hexadecimal format for each color component.</p>

  <h3>Features</h3>
<ul>
    <li>Converts individual RGB values to a two-digit hexadecimal string.</li>
    <li>Ensures RGB values are clamped within the 0-255 range.</li>
    <li>Combines the hexadecimal values of Red, Green, and Blue components into a single HEX color code.</li>
    <li>Easy to integrate and use in other Python projects.</li>
</ul>

<h3>Example Usage</h3>

    <p>Below are examples demonstrating the usage of the RGB to HEX color converter function:</p>

    <h3>Example 1: Convert RGB (255, 255, 255) to HEX</h3>
    <pre><code>    
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

# Example 1
hex_value = rgb(255, 255, 255)
console.log(`RGB (255, 255, 255) converts to HEX: ${hex_value}`);  // Output: FFFFFF
    </code></pre>

    <h3>Example 2: Convert RGB (0, 128, 192) to HEX</h3>
    <pre><code>    
// Example 2
hex_value = rgb(0, 128, 192)
console.log(`RGB (0, 128, 192) converts to HEX: ${hex_value}`);    // Output: 0080C0
    </code></pre>
  
  

</body>
</html>
