"""
Exercise 7: Check if a value exists in a dictionary
"""
sample_dict = {'a': 100, 'b': 200, 'c': 300}

a = list(filter(lambda x: sample_dict[x]==200,sample_dict))
b = [*filter(lambda x: x==200,sample_dict.values())]

print(any(a), any(b))