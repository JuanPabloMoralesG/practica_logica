"""
Exercise 6: Copy specific elements from one tuple to a new tuple
"""
tuple1 = (11, 22, 33, 44, 55, 66)

tp = tuple(filter(lambda x:x ==44 or x==55,tuple1))
print(tp)