"""
print the exceptions:
3
1 0
2 $
3 1
"""

n = int(input())
for _ in range(n):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:",e)