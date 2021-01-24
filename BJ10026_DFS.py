N= int(input())
map = [[False for j in range(N)] for i in range(N)]
for i in range(N):
    map[i] = list(input())

checkmap = [[False for j in range(N)] for i in range(N)]
cnt = 0
direction = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(N):
    for j in range(N):
        #print(i,j,checkmap[i][j])
        if checkmap[i][j] == False:
            check=[[i,j]]
            checkmap[i][j] =True
            while check != []:
                temp = check.pop(0)
                color = map[temp[0]][temp[1]]
                #print(color, temp[0], temp[1], 'color temp')
                for dir in direction:
                    x_n = dir[0] + temp[0]
                    y_n = dir[1] + temp[1]
                    if x_n >= N or x_n < 0 or y_n >= N or y_n <0 : continue
                    #print(x_n, y_n, map[x_n][y_n], checkmap[x_n][y_n])
                    if map[x_n][y_n] == color and checkmap[x_n][y_n] == False:
                        checkmap[x_n][y_n] = True
                        check.append([x_n,y_n])
                        #print(x_n, y_n, check, 'append')
                #print(checkmap)
            cnt +=1
cnt_RG = 0
checkmap = [[False for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if checkmap[i][j] == False:
            check=[[i,j]]
            checkmap[i][j] =True
            while check != []:
                temp = check.pop(0)
                color = map[temp[0]][temp[1]]
                if color == 'R' or color == 'G':
                    for dir in direction:
                        x_n = dir[0] + temp[0]
                        y_n = dir[1] + temp[1]
                        if x_n >= N or x_n < 0 or y_n >= N or y_n <0 : continue
                        if ( map[x_n][y_n] == 'R' or map[x_n][y_n] == 'G')  and checkmap[x_n][y_n] == False:
                            checkmap[x_n][y_n] = True
                            check.append([x_n,y_n])
                else:
                    for dir in direction:
                        x_n = dir[0] + temp[0]
                        y_n = dir[1] + temp[1]
                        if x_n >= N or x_n < 0 or y_n >= N or y_n <0 : continue
                        if map[x_n][y_n] == color  and checkmap[x_n][y_n] == False:
                            checkmap[x_n][y_n] = True
                            check.append([x_n,y_n])
            cnt_RG +=1
print("{0} {1}".format(cnt, cnt_RG))



##########################################################################################################

import sys
sys.setrecursionlimit(50000)
def dfs(x, y, color, mapping):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not isvisited[nx][ny] and mapping[nx][ny] == color:
            isvisited[nx][ny] = 1
            dfs(nx, ny, color, mapping)



n = int(input())
maps = []

for i in range(n):
    maps.append(sys.stdin.readline().rstrip())
colorBlindmaps=[]
for ma in maps:
    colorBlindmaps.append(ma.replace("R","G"))

normal = 0
isvisited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        color = maps[i][j]
        if not isvisited[i][j]:
            dfs(i, j, color, maps)
            normal += 1

colorBlind = 0
isvisited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        color = colorBlindmaps[i][j]
        if not isvisited[i][j]:
            dfs(i, j, color, colorBlindmaps)
            colorBlind+= 1

print(str(normal) + " " + str(colorBlind))
