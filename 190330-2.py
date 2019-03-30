def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else: result.append(right.pop(0))
    if len(left)>0:
        result.extend(left)
    if len(right)>0:
        result.extend(right)
    return result
def merge_sort(m):
    if len(m)<=1: return m
    mid=len(m)//2
    left=m[:mid]
    right=m[mid:]
    print('both',left,right)
    left=merge_sort(left)
    print('left',left,right)
    right=merge_sort(right)
    print('right',left,right)
    return merge(left,right)
m=[2,3,1,7,5]
print(merge_sort(m))
