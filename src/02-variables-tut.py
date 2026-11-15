# Variables
x = 5
y = "Hello, World!"

# In Python, a variable is created when you assign a value to it
# Python has no command for declaring a variable.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))



# Variable names are case-sensitive.
# This will create two variables
a = 4
A = "Sally"
#A will not overwrite a


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# In the print() function, you output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error
x = 5
y = "John"
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types
x = 5
y = "John"
print(x, y)


# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)