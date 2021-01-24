def fib(a,b,K):
    if K==1:
        return a
    if K==2:
        return b
    return fib(a,b,K-1)+fib(a,b,K-2)

print(fib(31,73,12))
print(fib(119,200,14))
print(fib(199,209,16))
