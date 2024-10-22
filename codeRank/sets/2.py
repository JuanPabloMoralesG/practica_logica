"""
add 1 for elements in A or -1 for elements in B
3 2
1 5 3
3 1
5 7
"""
n = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happyness = 0

for i in arr:
    if i in A:
        happyness += 1
    elif i in B:
        happyness += -1

print(happyness)