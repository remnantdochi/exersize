from itertools import combinations

height = [0 for _ in range(9)]
for i in range(9):
    height[i] = int(input())

comb = combinations(height,7)

for  c in comb:
    total = sum(c)
    if total == 100:
        ans= sorted(list(c))
        for a in ans:
            print(a)
        break
