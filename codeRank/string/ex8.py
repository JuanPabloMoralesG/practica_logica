"""
Sample Input

17
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
 ...
"""


def print_formatted(number):
    # your code goes here
    a = ""
    for i in range (1,number+1):
        w = len(bin(number)[2:])
        a = a +f"{str(i).rjust(w, ' ')} {oct(i)[2:].rjust(w, ' ')} {hex(i)[2:].rjust(w, ' ')} {bin(i)[2:].rjust(w, ' ')}\n"
    print(a)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)