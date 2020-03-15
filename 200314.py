#######################Question 1###################################
# N = int(input())
# if N%2 == 0:
#     temp = '1'*(N//2)
# else:
#     temp = '7'+'1'*((N-3)//2)
# print(temp)

#######################Question 2###################################
import sys
T=int(input())
dir = [[[0,1],[1,1],[1,0]],[[0,1],[-1,1],[-1,0]],[[0,-1],[-1,-1],[-1,0]],[[0,-1],[1,-1],[1,0]]]
def solution(x,y):
    sol_flag = 0
    for i in range(4):
        if sol_flag ==1:break
        pos_here = 0
        for d in dir[i]:
            new_x,new_y = d[0],d[1]
            print(new_x,new_y)
            if 0<=new_x<N and 0<=new_y<M and maps[new_x][new_y] == 1: pos_here+=1
        if pos_here == 3:
            check[x][y]= True
            for d in dir[i]:
                new_x,new_y = d[0],d[1]
                check[new_x][new_y] = True
            sol_flag =1

    if sol_flag ==0: return False
    else: return True

for t in range(T):
    N, M = map(int,input().split()) #N이 행 M이 열
    maps=[[] for _ in range(N)]
    check=[[False for _ in range(M)] for _ in range(N)]
    flag = 1
    for i in range(N):
        maps[i] = list(map(int,sys.stdin.readline().split()))

    for i in range(N):
        if flag == 0: break
        for j in range(M):
            if maps[i][j] == 1 and check[i][j] == False:
                if solution(i,j)==False:
                    flag = 0
                    break
    if flag == 0: print('NO')
    else : print('YES')

#######################Question 3###################################
# N, K = map(int,input().split())
# array = list(map(int,input().split()))
# print(array[(N-K)]-array[0])
