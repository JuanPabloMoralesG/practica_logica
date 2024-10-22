"""
N notas
X estudiantes
average = sum(promedios)/allstudents


N, X = list(map(int, input().split()))
S = [list(map(float, input().split())) for _ in range(X)]
print(*["%.1f" %(sum(i)/X) for i in zip(*S)], sep='\n')

"""

N, X = list(map(int,input().split()))
scores = []
for i in range(int(X)):
    scores.append(list(map(float,input().split())))

for i in zip(*scores):
    print(i)
    print(sum(i)/X)