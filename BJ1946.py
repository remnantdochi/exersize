T= int(input())
for _ in range(T):
    N = int(input())
    nlist = []
    for i in range(N):
        s1,s2 = map(int,input().split())
        nlist.append([s1,s2])
    nlist.sort(key=lambda element : element[0])
    ans = 0
    minscore = N+1
    for i in range(N):
        if minscore > nlist[i][1] :
            ans +=1
            minscore = nlist[i][1]

    print(ans)
