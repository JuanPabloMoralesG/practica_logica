"""
print simetric diference
4
2 4 5 9
4
2 4 11 12
"""
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))

s = a.symmetric_difference(b)
print(*sorted(s),sep="\n")