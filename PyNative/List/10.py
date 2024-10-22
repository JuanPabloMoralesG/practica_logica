"""
Exercise 10: Remove all occurrences of a specific item from a list.
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
l = [*filter(lambda x: x!= 20,list1)]
print(l)