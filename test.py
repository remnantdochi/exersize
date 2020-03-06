
#abc=list(map(int,input().split(' ')))
#print(abc)
#print({0}.format(abc[i] i for i in range(len(abc))))


sol=[[0,1,0],[0,0,0],[1,0,1]]

sol[1] = [1 if sol[0][k] == 1 else 0 for k in range(3)]

sol[2] = sol[0]+sol[1]+sol[2]
print(sol[2])
