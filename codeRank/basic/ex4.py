"""
N Total de numeros en la lista
Condition 1: All the integers in the list are positive.
Condition 2: is a palindromic integer.

5
12 9 61 5 14
"""

N = int(input())
nums = list(map(int,input().split()))
print(all(list(map(lambda x:x>0,nums)))and any(list(map(lambda x: str(x)== str(x)[::-1],nums))))