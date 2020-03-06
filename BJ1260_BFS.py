def DFS(start,now,check):
    if check[now] == 1: return
    check[now] = 1
    print(now, end = " ")
    for item in sol[now]:
        DFS(start,item,check)

N,M,V = map(int,input().split(" "))
maps = [[]for _ in range(N+1) ]
sol = [[] for _ in range(N+1)]
for i in range(M):
    n1,n2 = map(int, input().split(" "))
    maps[n1].append(n2) ##이러지 말고 [ 0 0 0 *N]으로 해서 1로 만들면 sort할 필요 없으
    maps[n2].append(n1)
    #print(maps)
for i in range(N+1):
    sol[i] = sorted(maps[i])

#print(sol)

print(V, end= " ")
s_line = sol[V]
check_DFS = [0 for _ in range(N+1)]
check_DFS[V] = 1
for s in s_line:
    DFS(V,s,check_DFS)
print()

print(V, end = " ")
que=sol[V]
#print("test1",que)
check_BFS = [0 for _ in range(N+1)]
check_BFS[V] = 1
while que !=[]:
    #print(que)
    item = que.pop(0)
    if check_BFS[item] == 1: continue
    check_BFS[item] = 1
    print(item, end= " ")
    #print(maps[item])
    que.extend(sol[item]) #큐에 넣기 전에 확인을 하는게 메모리 절약을 할 수 있겠다
