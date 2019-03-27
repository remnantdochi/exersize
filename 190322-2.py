def longestPalindrome(s: str) -> str:
    memo=[[None]*len(s)]*len(s)
    maxlen=1
    for i in range(len(s)):
        memo[i][i]=True
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            memo[i][i+1]=True
            maxlen=2
            result=
        else: memo[i][i+1]=False
    '''
    def check(i,j):
        if memo[i+1][j-1] == None:
            check(i+1,j-1)
        if memo[i+1][j-1] == True:
            if s[i]==s[j]:
                memo[i][j]=True
            else: memo[i][j] =False
            return memo[i][j]'''
    for i in range(len(s)):
        for j in range(len(s)-1):
            if s[i]==s[j] and memo[i+1][j-1] == True:
                memo[i][j]=True
                temp=j-i+1
                if temp>maxlen:
                    maxlen=temp
                    result=s[i][j+1]
            else: memo[i+1][j-1]=
