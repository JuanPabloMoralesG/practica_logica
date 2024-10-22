"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""


if __name__ == '__main__':
    N = int(input())

    l = []
    for i in range(N):
        exp =input().split()
 
        if exp[0]== "insert":
            l.insert(int(exp[1]),int(exp[2]))
        elif exp[0]=="remove":
            l.remove(int(exp[1]))
        elif exp[0]=="append":
            l.append(int(exp[1]))
        elif exp[0]=="sort":
            l.sort()
        elif exp[0]=="pop":
            l.pop()
        elif exp[0]=="reverse":
            l.reverse()
        else:
            print(l)