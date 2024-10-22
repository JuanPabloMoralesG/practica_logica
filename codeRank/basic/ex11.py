if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        students.append(input())
        scores.append(float(input()))


    second = sorted(set(scores))[1]
    d = list(filter(lambda x:x[1]==second,zip(students,scores)))
    out = list(sorted(map(lambda x:x[0],d)))
    print(*out,sep="\n")