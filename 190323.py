def maxSubArray(nums):
    result=[]
    s=0;i=1
    while (i<len(nums)):
        temp=sum(nums[s:i])
        print(s,i,temp)
        if temp<0:
            result.append(0)
            s=i
        else: result.append(sum(nums[s:i]))
        i=i+1
    return max(result)
test1= [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(test1))
