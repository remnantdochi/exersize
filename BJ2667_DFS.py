#20200103

import sys
sys.setrecursionlimit(50000)


'''입력형태 띄어쓰기 없이
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
def DFS(x,y,maps,housenum):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    for k in range(4):
        nx = x+ dx[k]
        ny = y+ dy[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and maps[nx][ny] == '1':
            #print(sx,sy,x,y,nx,ny,'maps 1','k:',k)
            visited[nx][ny] = True
            housenum = DFS(nx, ny, maps,housenum+1)
        #else:
            #print(sx,sy,x,y,nx,ny,'maps 0','k:',k)

    #print(sx,sy,x,y,nx,ny,'before return')
    #print(housenum)
    return housenum

n = int(input())
maps = []
for i in range(n):
    maps.append(sys.stdin.readline().rstrip())
house = []
cnt = 0

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == '1' and visited[i][j] == False:
            visited[i][j] = True
            house.append( DFS(i,j,maps,1))

house.sort()
print(len(house))
for i in range(len(house)):
    print(house[i])
