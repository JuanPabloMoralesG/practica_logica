n = int(input())

print(*list(map(lambda x: pow(x,2),range(0,n))),sep="\n")