def solution(drum):
    answer = 0
    n = len(drum)
    for i in range(n):
        x,y=0,i
        cnt=0
        print('i',i)
        while (x!=n and cnt != 2):
            print(x,y,cnt)
            if drum[x][y] == '#' : x+=1
            elif drum[x][y] == '>' : y+=1
            elif drum[x][y] == '<' : y-=1
            elif drum[x][y] == '*':
                cnt+=1
                x+=1
        if x == n: answer+=1
    return answer
# def finding(x,y,cnt,n,drum):
#     #print(x,y,cnt,drum[x][y])
#     #print(x,y)
#     if x == n :
#         return 1
#     if drum[x][y] == '#':
#         return finding(x+1,y,cnt,n,drum)
#     if drum[x][y] == '<':
#         return finding(x,y-1,cnt,n,drum)
#     if drum[x][y] == '>':
#         return finding(x,y+1,cnt,n,drum)
#     if drum[x][y] == '*':
#         if cnt == 0: return finding(x+1,y,cnt+1,n,drum)
#         else :
#             return 0

solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"])
