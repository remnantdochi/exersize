import sys
from collections import deque
#시간초과 뜬다 일단 BackTracking 이하 BT배우고 온다
R, C = map(int, input().split())
maps = [[] for _ in range(R)]

dir = [[0,1], [1,0], [-1,0], [0,-1]]
##caution : python에는 이미 map이라는게 존재!!
for i in range(R):
    maps[i] = list(sys.stdin.readline().rstrip())
#print(maps)
alpha = deque()
alpha.append([maps[0][0]])

res = 0
def function(x, y, alpha,cnt):
    global res
    #print(cnt, x,y,res,alpha)
    res = max(res, len(alpha))
    for d in dir:
        new_x, new_y = x+d[0], y+d[1]
        if 0<= new_x < R and 0<= new_y < C:
            #print(new_x,new_y)
            if maps[new_x][new_y] not in alpha:
                alpha.append(maps[new_x][new_y])
                function(new_x, new_y, alpha,cnt+1)
                alpha.pop()
    #print('before return',alpha)
    #return alpha
function(0,0,alpha,0)
print(res)


#string = " ".join(list1) list를 string으로!
#list1 =list(string) string을 list로!
