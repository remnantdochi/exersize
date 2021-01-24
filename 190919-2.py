def twoSum(numbers,target):
        a={}
        for index,i in enumerate(numbers):
            if target-i in a:
                return a[target-i]+1,index+1
            print(a)
            a[i]=index
print(twoSum([1,2,3,7],9))

#뒤가 아니라 앞을 비교하는것
