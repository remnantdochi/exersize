def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i=j=0
    result=[]
    print(nums1,nums2)
    while (i != len(nums1) and j != len(nums2)):
        print(i,j,result)
        if nums1[i] == nums2[j] :
            print('t1')
            if nums1[i] not in result:
                result.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] > nums2[j] :
            print('t2')
            j+=1
        else :
            print('t3')
            i+=1
    return result

print(intersection([4,9,5],[9,4,9,8,4]))
