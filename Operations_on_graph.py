def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
k = I()
adjMatrix = [[] for _ in range(n)]
for _ in range(k):
    operation,*vertice = IL()
    if operation == 1:
        a,b = vertice
        adjMatrix[a-1].append(b)
        adjMatrix[b-1].append(a)
    elif adjMatrix[vertice[0]-1]:
        print(*adjMatrix[vertice[0]-1])