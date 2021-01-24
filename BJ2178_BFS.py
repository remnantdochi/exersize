import sys
from collections import deque

read = sys.stdin.readline

N,M=map(int,read().split())
map=[0 for _ in range(N)]
cnt = [[-1 for _ in range(M)] for _ in range(N)]
dir = [[0,1],[0,-1],[1,0],[-1,0]]
cnt[0][0] = 1
for i in range(N):
    map[i]= read().rstrip()

x,y=0,0

q=deque()
q.append([x,y])
while q:
    for _ in range(len(q)):
        item=q.popleft()
        x,y=item[0],item[1]
        for d in dir:
            new_x,new_y=x+d[0],y+d[1]
            if 0<=new_x<N and 0<=new_y<M and map[new_x][new_y] == '1':
                if cnt[new_x][new_y] == -1:
                    cnt[new_x][new_y] = cnt[x][y]+1
                    q.append([new_x,new_y])
print(cnt[N-1][M-1])
