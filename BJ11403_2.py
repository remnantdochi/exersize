#예시
'''
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
'''

def DFS(start,now,check):
    if check[now] == 1:
        return
    check[now] = 1
    sol[start][now] = '1'
    for item in maps[now]:
        DFS(start,item,check)

n = int(input()) ###7
maps = [[] for _ in range(n)]
sol = [['0' for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int,input().split()))
    maps[i] = [j for j in range(n) if temp[j] == 1] ###maps[0] = [3]

##여기까지 사전 준비

for i in range(n): #0번쨰 노드부터 sol 진행
    check = [0 for _ in range(n)] #방문했는지를 기억하기 위한 check는 start에 해당하는것
    s_line = maps[i] ###s_line = [3]
    for j in maps[i]:
        DFS(i,j,check)
        # if j<i: ##만약 1번째 노드하는데 0번째 노드 값이 나오면 0번째 노드 경로 그대로 학습 #이거보류...


##최종적으로는 sol 변환해서 할거임
for i in range(n):
    print(" ".join(sol[i])) #str만 사용가능 
