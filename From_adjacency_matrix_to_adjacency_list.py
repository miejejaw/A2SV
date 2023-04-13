def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
for _ in range(n):
    row = IL()
    ans = []
    for ind in range(n):
        if row[ind] == 1:
            ans.append(ind+1)
    print(len(ans),*ans)