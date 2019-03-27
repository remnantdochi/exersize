def peakIndexInMountainArray(A):
    n=len(A)
    def searchbin(s,index,e):
        leftc=(A[index]-A[index-1])
        rightc=(A[index+1]-A[index])
        print(s,index,e)
        print(leftc,rightc,A[index])
        if leftc * rightc <0 :
            print(index)
            return index
        elif leftc>0:
            print('test1')
            return searchbin(index,(index+e)//2,e)
        elif leftc<0:
            print('test2')
            return searchbin(s,(s+index)//2,index)
    return searchbin(0,n//2,n)
peakIndexInMountainArray([40,48,61,75,100,99,98,39,30,10])
