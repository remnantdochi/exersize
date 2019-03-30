def subset(a,k,n):
    if k==n: print(a)
    else:
        a[k]=0
        subset(a,k+1,n)
        a[k]=1
        subset(a,k+1,n)
a=[0]*3
#subset(a,0,3)

def permutation(order,k,n):
    if k==n: print(order)
    else:
        check=[False]*n
        for i in range(k):
            check[order[i]]=True
        for i in range(n):
            if check[i]==False:
                order[k]=i
                permutation(order,k+1,n)
order=[1,2]
#permutation(order,0,2)

a=[1,2,3]
def perm(n,k):
    if k==n: print(a)
    else:
        for i in range(k,n):
            print('test1',k,i,n)
            a[k],a[i]=a[i],a[k]
            print('test1',a)
            perm(n,k+1)
            print('test2',k,i,n)
            a[k],a[i]=a[i],a[k]
            print('test2',a)
perm(3,0)
