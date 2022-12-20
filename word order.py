from collections import defaultdict
n = int(input())
def d(): return 0
dic = defaultdict(d)

for _ in range(n):
    dic[input()] += 1
    
print(len(dic))
print(*dic.values())
