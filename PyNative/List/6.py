"""
Exercise 6: Remove empty strings from the list of strings
"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
l = [*filter(lambda x: x!="" ,list1)]
print(l)