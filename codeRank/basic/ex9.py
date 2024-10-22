"""
Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    ls = list(filter(lambda x: sum(x) != n,l))
    print(l)
    print(ls)