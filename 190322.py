def longestPalindrome(s: str) -> str:
    result=[]
    for i in range(len(s)-1):
        for j in range(len(s),i,-1):
            print(s[i:j])
            print(check(s[i:j]))
            if check(s[i:j]):
                result.append(s[i:j])
    lenresult=[len(i) for i in result]
    maxlen=lenresult.index(max(lenresult))
    return result[maxlen]
def check(particle):
    if len(particle) == 0 or len(particle) == 1:
        return True
    else:
        if particle[0]==particle[-1]:
            return check(particle[1:len(particle)-1])
        else: return False
print("result",longestPalindrome("babad"))
