"""
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Sample Input: Sorting1234
Sample Output: ginortS1324

"""
S = input()
#print(sorted(S, key=lambda x:(x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x)))
U = sorted([i for i in S if i.isupper()])

E = filter(S,lambda x: x.isdigit() and int(x)%2 == 0)

print(U,E)