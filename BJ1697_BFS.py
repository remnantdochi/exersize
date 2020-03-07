N, K = map(int, input().split())
arr = [-1 for _ in range(100001)]
arr[N] = 0
q=[N]
check=0
while q:
    if check==1:break
    i = q.pop(0)
    for j in (i-1,i+1,i*2):
        if 0<=j<100001:
            if arr[j] ==-1:
                arr[j]= arr[i]+1
                if j==K:
                    check=1
                    break

                q.append(j)
print(arr[K])
    #
    # for item in (i-1,i+1,i*2):
    #     if 0<=item<100001:
    #         if arr[item] == 0:
    #             if item>K:
    #                 if item==i-1:
    #                     arr[item] = arr[i]+1
    #                     q.append(item)
    #                 else : break
    #             elif item == K:
    #                 arr[K]=arr[i]+1
    #                 check=1
    #                 break
    #             else:
    #                 arr[item] = arr[i]+1
    #                 q.append(item)



# def bfs(v):
#     visited = [False]*100001
#     q=[v]
#     cnt=0
#     state=False
#     while q:
#         for _ in range(len(q)): //이거 하나로 값이 달라지는데 왜지?
#
    #         v=q.pop(0)
    #         if not (visited[v]):
    #             visited[v]=True
    #             if v==K:
    #                 state = True
    #                 break
    #             if v-1>=0:
    #                 q.append(v-1)
    #             if v+1<=100000:
    #                 q.append(v+1)
    #             if v*2<=100000:
    #                 q.append(v*2)
    #         if state:
    #             print(cnt)
    #             break
    #         cnt+=1
# N,K=map(int,input().split())
# bfs(N)
