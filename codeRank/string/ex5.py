
if __name__ == '__main__':
    s = input()
    s = list(s)
    out = []
    out.append(any(map(lambda x:x.isalnum(),s)))
    out.append(any(map(lambda x:x.isalpha(),s)))
    out.append(any(map(lambda x:x.isdigit(),s)))
    out.append(any(map(lambda x:x.islower(),s)))
    out.append(any(map(lambda x:x.isupper(),s)))

    print(*out,sep="\n")