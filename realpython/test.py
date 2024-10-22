"""
verify a list in a range
"""
def check_range(numbers, min_val, max_val):
    return all([*map(lambda x: x>min_val and x<max_val,numbers)])

print(check_range([1,2,3,40],0,5))