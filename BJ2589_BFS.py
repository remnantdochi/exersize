import sys
from collections import deque
read = sys.stdin.readline
#L : land // W : water
dir = [[0,1],[0,-1],[1,0],[-1,0]]
M,N = map(int,read().split())
map=[0 for _ in range(M)]
for i in range(M):
    map[i] = read().rstrip()
ans =0

def BFS(a,b):
    distance = 0
    q=deque()
    q.append([a,b])
    check[a][b]=0
    while q:
        item=q.popleft()
        x,y=item[0],item[1]
        #print('item',x,y)
        for d in dir:
            new_x,new_y= x+d[0],y+d[1]
            if 0<=new_x<M and 0<=new_y<N:
                if check[new_x][new_y]==-1 and map[new_x][new_y] == 'L':
                    #distance +=1
                    check[new_x][new_y] = check[x][y] +1
                    #print('new',new_x,new_y,check[new_x][new_y])
                    distance = max(distance,check[new_x][new_y])
                    q.append([new_x,new_y])
    return distance

for i in range(M):
    for j in range(N):
        if map[i][j] == 'L':
            check = [[-1 for _ in range(N)] for _ in range(M)]
            ans = max(BFS(i,j),ans)

print(ans)
