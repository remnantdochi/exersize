n = int(input())
res = 0
maps = [[0 for _ in range(n)] for _ in range(n)]
#maps = [0 for _ in range(n)]
def possible(cnt, candidate, check):
    #print(cnt, candidate,check)
    for i in range(cnt):
        if candidate[i][1] == check: return False
        if abs(candidate[i][1] - check) == abs(cnt-candidate[i][0]) : return False
    return True
def BT(cnt, candidate):
    global res
    if cnt == n:
        res +=1
        #print(candidate)
        return
    for i in range(n):
        if possible(cnt, candidate, i):
            candidate.append([cnt,i])
            BT(cnt+1, candidate)
            candidate.pop()

BT(0,[])
print(res)
