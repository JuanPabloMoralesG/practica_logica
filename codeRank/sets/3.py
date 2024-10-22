"""
number of contries:
7
UK
China
USA
France
New Zealand
UK
France 
"""
n = int(input())
s = set()
for i in range(n):
    s.add(input().strip().upper())

print(len(s))