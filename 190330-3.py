#A:list,l:start index, r:end index
def partition(A,l,r):
    p=A[l]
    i=l+1
    j=r
    while i<=j:
        while (i<=j) and (A[i]<=p): i+=1
        while (i<=j) and (A[j]>=p): j-=1
        print(i,j)
        if i<=j:
            A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    return j
def quicksort(A,l,r):
    if l<r:
        s=partition(A,l,r)
        print('test1',s,A,l,r)
        quicksort(A,l,s-1)
        print('test2',s,A,l,r)
        quicksort(A,s+1,r)
A=[5,4,3,2,1]
quicksort(A,0,len(A)-1)
print(A)
