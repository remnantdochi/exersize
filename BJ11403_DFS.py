#20200107

import sys
sys.setrecursionlimit(50000)
'''입력형태 띄어쓰기 존재
3
0 1 0
0 0 1
1 0 0
'''
n = int(input())
maps = [[] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
sol = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    maps[i]=list(map(int,sys.stdin.readline().rstrip().split()))

graph = [[] for _ in range(n)]
#전처리 과정
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            print(i,j)
            graph[i].append(j)

print(graph)

def DFS(sx,x,y):
    print(sx,x,y)
    sol[sx][y] = 1
    print(sol[x])
    if graph[y] != []:
        print(graph[y])
        for item in graph[y]:
            if item ==sx:
                sol[sx][sx] = 1
                return
            DFS(sx,y,item)
    else : return

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0 : continue
        DFS(i,i,j)

print(sol)
