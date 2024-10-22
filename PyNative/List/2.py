"""
Zip the lists
"""

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

l4 = [*map(lambda x: x[0]+x[1],zip(list1,list2))]
print(l4)