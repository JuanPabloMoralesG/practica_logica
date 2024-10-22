"""
make:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
"""
len_l = int(input())
s = set(map(int,input().split()))
n = int(input())
d = []
for _ in range(n):
    d.append(input().split())

for i in d:
    if i[0] == "pop":
        s.pop()
    elif i[0] == "remove":
        s.remove(int(i[1]))
    elif i[0] == "discard":
        s.discard(int(i[1]))

print(sum(s))