def majority(nums):
    check=dict()
    for i in nums:
        if i not in check:
            check[i]=1
        else:
            check[i]+=1
    print(check)
    for key,val in check.items():
        if val > len(nums):
            return key

print(majority([3,2,3]))
