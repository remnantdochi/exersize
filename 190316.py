N=int(input())
divisions=[]
for i in range(1,N//2+2):
    if N % i == 0 :
        divisions.append((i,N//i))
print(divisions)
results=[]
for divs in divisions:
    results.append(abs(divs[0]-divs[1]))
print(min(results))
