import sys

print(sys.version)
print("Hello, World!")
# Indentation is required - Python uses indentation to indicate a block of code.
if 5 > 2:
    print("Five is greater than two!")
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
if 5 > 2:
    print("Five is greater than two!")
    print("Test!")
    
# Print Without a New Line
print("Hello World!", end=" ")
print("I will print on the same line.")

# Math
print(3 + 3)
print(2 * 5)

# Mix Text and Numbers
print("I am", 35, "years old.")

# Multiline Comments
"""
This is a comment
written in
more than just one line
"""