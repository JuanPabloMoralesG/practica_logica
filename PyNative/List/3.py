"""
Exercise 3: Turn every item of a list into its square
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
print([*map(lambda x: pow(x,2),numbers)])