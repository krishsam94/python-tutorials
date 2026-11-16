# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# Loop Through the Index Numbers
for i in range(len(thislist)):
  print(thislist[i])
# The iterable created in the example above is [0, 1, 2].


# Using a While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]