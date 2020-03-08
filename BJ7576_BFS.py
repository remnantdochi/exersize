import sys
from collections import deque
M, N = map(int,input().split())
maps=[[] for _ in range(N)]
check=[[False for _ in range(M)] for _ in range(N)]

##흑흑 sys.stdin.readline()을 생활화하자
#print(check[1][2])
total = M*N
cnt=-1
dir = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(N):
    maps[i] = list(map(int,sys.stdin.readline().split()))

que = deque()
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            que.append([i,j])
            total-=1
        elif maps[i][j] == -1: total-=1
if total == 0: cnt=0
while que and total != 0:
    flag=0
    #print('que',que)
    for _ in range(len(que)):
        item = que.popleft()
        x,y=item[0],item[1]
        if check[x][y]==False :
            #print('item',item)
            flag=1
            check[x][y] = True
            if maps[x][y] == -1:continue
            elif maps[x][y] == 0: total-=1
            for new_d in dir:
                new_x = new_d[0]+x
                new_y = new_d[1]+y
                if 0<=new_x<N and 0<=new_y<M:
                    if check[new_x][new_y] == False: que.append([new_x,new_y])
    if flag==1:
        cnt+=1
    #print(flag,cnt)
#print(cnt,total)
if total == 0: print(cnt)
else : print(-1)
