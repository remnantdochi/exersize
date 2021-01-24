'''#내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

N = int(input())
row = [0 for _ in range(N)]
result = 0
dfs(0)
print(result)'''

n = int(input())
res = 0
#maps = [[0 for _ in range(n)] for _ in range(n)]
row = [0 for _ in range(n)]
def possible(cnt, x):
    #print(cnt,x)
    for i in range(cnt):
        if row[i]==x : return False
        if abs(row[i]-x) == cnt-i: return False
    #print(cnt,x,row)
    return True
def BT(cnt):
    global res
    if cnt == n:
        res +=1
        #print(row)
        return
    for i in range(n):
        if possible(cnt,i):
            row[cnt] = i #cnt가 행 i는 선택된 열
            BT(cnt+1)

BT(0)
print(res)
