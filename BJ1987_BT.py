R, C = map(int, input().split())
maps = [[] for _ in range(R)]
for i in range(R):
    maps[i] = list(input())

alpha = [0]*26
dir = [[0,1],[1,0],[-1,0],[0,-1]]

start = ord(maps[0][0])-ord('A')
alpha[start] = 1
res = 0

def BT(x,y):
    global res
    cnt=0
    if x==R-1 and y==C-1:
        for i in range(len(alpha)):
            if alpha[i] == 1: cnt+=1
        res = max(res, cnt)
        #print('if end of map')
        return

    for d in dir:
        new_x, new_y = x+d[0], y+d[1]
        if 0<=new_x<R and 0<=new_y<C:
            #print(x,y,new_x,new_y)
            index = ord(maps[new_x][new_y])-ord('A')
            if alpha[index] == 0:
                alpha[index] = 1
                #print('before BT', alpha)
                BT(new_x, new_y)
                #print('after BT', alpha)
                alpha[index] = 0

    for i in range(len(alpha)):
        if alpha[i] == 1: cnt+=1
    res = max(res, cnt)
    return
BT(0,0)
print(res)
