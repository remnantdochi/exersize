#https://rebas.kr/761
# a = [[0]*N]*N 할경우 값이 복사되지만 일차행렬은 괜찮음
# 왜 일차행렬이냐 링크에서 보면 대각선에 해당하는 값에 어떤 row 존재할경우 그 줄 자체가 안돼니까 해당하는 값을 행렬로 표현

N =int(input())
res = 0

ver, left, right = [0]*N, [0]*(2*N-1), [0]*(2*N-1)

def BT(row):
    global res
    if row==N:
        res+=1
        return
    for col in range(N):
        if ver[col] + left[row+col] + right[row-col+N-1]==0:
            ver[col]=left[row+col]=right[row-col+N-1]=1
            BT(row+1)
            ver[col]= left[row+col]= right[row-col+N-1] = 0

BT(0)
print(res)
