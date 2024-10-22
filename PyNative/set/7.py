"""
Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
Given:
"""
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set1.intersection_update(set2)
print(set1)