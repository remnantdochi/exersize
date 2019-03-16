row1=int(input())
header1=list(map(str,input().split(' ')))
table1=dict()
for i in range(1,row1):
    temp=list(map(str,input().split(' ')))
    table1[int(temp[0])]=[temp[1],temp[2]]
row2=int(input())
header2=list(map(str,input().split(' ')))
table2=dict()
for i in range(1,row2):
    temp=list(map(str,input().split(' ')))
    table2[int(temp[0])]=[temp[1],temp[2]]
#print(table1,table2)
#############printing
print(" ".join(map(str, header1+header2[1:])))
for i in range(1,row1):
    if i not in table2:
        table1[i].append('NULL')
        table1[i].append('NULL')
        print(" ".join(map(str, table1[i])))
    else:
        print(" ".join(map(str, table1[i]+table2[i])))
