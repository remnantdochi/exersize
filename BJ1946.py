import sys

T= int(input())
for _ in range(T):
    N = int(input())
    nlist=[[*map(int,sys.stdin.readline().split())] for _ in range(N)]
    nlist.sort(key=lambda element : element[0])
    ans = 0
    minscore = N+1
    for i in range(N):
        if minscore > nlist[i][1] :
            ans +=1
            minscore = nlist[i][1]

    print(ans)
