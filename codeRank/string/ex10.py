"""
AABCAAADA
3
"""
def filt(str):
    t = ""
    for i in str:
        if i not in t:
            t = t + i
    return t
def merge_the_tools(string:str, k:int):
    l = []
    cont = 1
    sub = ""
    for i in string:
        if cont < k:
            sub= sub +i
            cont += 1
        elif cont == k:
            sub= sub +i
            l.append(sub)  
            sub = ""
            cont = 1
        else:
            cont += 1
    print(*map(filt,l),sep="\n")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)