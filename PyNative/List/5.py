"""
Exercise 5: Iterate both lists simultaneously
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
l3 = [*zip(list1,list2)]

for i in l3:
    print(i[0],i[1])
