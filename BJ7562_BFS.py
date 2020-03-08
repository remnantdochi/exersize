from collections import deque
dir = [[2,1],[1,2],[2,-1],[1,-2],[-2,-1],[-2,1],[-1,-2],[-1,2]]
T=int(input())
for t in range(T):
    I = int(input())
    s_x,s_y = map(int,input().split())
    e_x,e_y = map(int,input().split())
    cnt = [[-1 for _ in range(I)] for _ in range(I)]
    cnt[s_x][s_y] = 0
    q=deque()
    q.append([s_x,s_y])
    flag=0
    while q:
        if flag==1:break
        for _ in range(len(q)):
            item=q.popleft()
            x,y=item[0],item[1]
            if x==e_x and y==e_y:
                flag=1
                break
            for d in dir:
                new_x,new_y=x+d[0],y+d[1]
                if 0<=new_x<I and 0<=new_y<I:
                    if cnt[new_x][new_y] == -1:
                        cnt[new_x][new_y] = cnt[x][y]+1
                        q.append([new_x,new_y])

    print(cnt[e_x][e_y])
