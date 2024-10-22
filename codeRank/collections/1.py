"""
fillter word and count them
"""
n = int(input())
l = []
out = []
for _ in range(n):
    s = input()
    if s not in l:
        out.append(1)
        l.append(s)
    else:
        i = l.index(s)
        out[i]+= 1
print(len(l))
print(*out)