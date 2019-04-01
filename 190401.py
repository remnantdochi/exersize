def maxSubArray(nums) -> int:
    result=[]
    start=0
    if len(nums)==0:return 0
    elif len(nums)==1: return nums[0]
    for i in range(1,len(nums)+1):
        temp=sum(nums[start:i])
        print(temp,start,i)
        if temp<0:
            start=i
            result.append(0)
        else:
            result.append(temp)
    print(result)
    return max(result)
maxSubArray([-2,1])
