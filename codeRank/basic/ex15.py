"""
Sort by upper, digit, even digit
Sorting1234
"""
s = input()
l = list(sorted(s,key=lambda x: (x.isdigit() and int(x)%2 == 0,x.isdigit(),x.isupper(),x)))
print("".join(x for x in l))