"""
Exercise 8: Rename key of a dictionary
"""
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
a = sample_dict.pop("city")
sample_dict["location"] = a
print(sample_dict)
