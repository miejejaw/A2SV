def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
sources = []
sinks = []
arr = []
for i in range(1,n+1):
    row  = IL()
    if sum(row) == 0:
        sinks.append(i)
    arr.append(row)
for i,row in enumerate(zip(*arr)):
    if sum(row) == 0:
        sources.append(i+1)
        
print(len(sources),*sources)
print(len(sinks),*sinks)
    
