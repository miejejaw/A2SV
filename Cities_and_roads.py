def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
ans = 0
for _ in range(n):
    ans += sum(IL())
    
print(ans//2)