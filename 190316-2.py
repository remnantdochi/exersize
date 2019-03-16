chemicals=input()
check=[chemicals[i].isdigit() for i in range(len(chemicals))]
checkinnum=[0 if digit==False else 1 for digit in check ]
if checkinnum.count(0) != checkinnum.count(1) :
    print('error')
else:
    result=[]
    p1,p2=0,len(chemicals)//2
    for i in range(len(chemicals)//2):
        result.append(chemicals[p1])
        if chemicals[p2] != '1':
            result.append(chemicals[p2])
        p1+=1;p2+=1
    print(''.join(result))
