T= int(input())
for _ in range(T):
    N = int(input())
    nlist = []
    for i in range(N):
        s1,s2 = map(int,input().split())
        nlist.append([s1,s2])
    nlist.sort(key=lambda element : element[0])
    ans = 0
    for i in range(N):
        flag = False
        for j in range(i):
            if nlist[i][1] > nlist[j][1]:
                flag = True
                break
        if flag != True: ans +=1
    print(ans)
