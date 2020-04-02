n = int(input())
A = list(map(str,input().split()))
numbers = [0]*10
max_r, min_r = 0,9876543210

def function(index,result,last):
    global max_r, min_r
    if index == n+1:
        max_r = max(max_r, result)
        min_r = min(min_r, result)
        #print('//final// index : ',index,'i ','result ' ,result)
        return
    for i in range(10):
        if index == 0:
            numbers[i] = 1
            result+=i*(10**(n-index))
            #print('for first! index : ',index,'i ', i, 'result ' ,result)
            function(index+1,result,i)
            numbers[i] = 0
            result-=i*(10**(n-index))
        elif numbers[i] == 0 :
            if (A[index-1] == '<' and last <i ) or ( A[index-1] == '>' and last > i):
                numbers[i] = 1
                result+=i*(10**(n-index))
                #print( 'index : ',index,'i ', i, 'result ' ,result)
                function(index+1,result,i)
                numbers[i] = 0
                result-=i*(10**(n-index))

function(0,0,0)
print(str(max_r))
if min_r < 10**n :
    print('0'+str(min_r))
else : print(str(min_R))
#print(max_r,min_r)
