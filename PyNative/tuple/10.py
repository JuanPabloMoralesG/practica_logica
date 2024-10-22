"""
Exercise 10: Check if all items in the tuple are the same
"""
tuple1 = (0, 0, 0, 0)

res = all(map(lambda x: x==0, tuple1))
print(tuple1.count(0)==len(tuple1))