#making permutation!
def permutate(nums):
    result=[]
    n=len(nums)
    def makeitem(length,item,rest):
        if length==n:
            result.append(item[:])
            return
        for i in range(len(rest)):
            item.append(rest[i])
            makeitem(length+1,item,rest[:i]+rest[i+1:])
            item.pop()
    makeitem(0,[],nums)
    #print(result)
    return result
permutate([1,2,3])
