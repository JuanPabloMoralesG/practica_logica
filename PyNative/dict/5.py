"""
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

dic = {k: sample_dict[k] for k in keys}
print(dic)