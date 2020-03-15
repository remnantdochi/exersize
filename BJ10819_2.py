import itertools
N= int(input())
array = list(map(int,input().split()))
result = itertools.permutations(array)
ans=0
for item in result:
    sum=0
    for i in range(1,N):
        sum+=abs(item[i]-item[i-1])
    ans = max(ans,sum)

print(ans)
