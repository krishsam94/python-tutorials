a = "Hello, World!"
print(a.upper())
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


print(a.replace("H", "J"))


# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)