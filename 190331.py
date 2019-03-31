def lazer(building):
    result=[]
    stack=[]
    ##빛을 왼쪽으로 쏘고 있다고 가정
    for i in range(len(building)):
        if i==0:
            stack.append((i,building[i]))
            result.append(0)
        else:
            while stack:
                temp=stack.pop()
                #print(temp,stack,building[i])
                if temp[1] >= building[i]:
                    result.append(i-temp[0])
                    stack.append(temp)
                    stack.append((i,building[i]))
                    break
            if stack == []:
                stack.append((i,building[i]))
                result.append(0)
                #print('',stack,result)

    result2=[]
    stack2=[]
    #print(result)
    for i in range(len(building)-1,-1,-1):
        if i==len(building)-1:
            stack2.append((i,building[i]))
            result2.append(0)
        else:
            while stack2:
                temp=stack2.pop()
                #print(temp,stack2,building[i])
                if temp[1] >= building[i]:
                    result2.append(temp[0]-i)
                    stack2.append(temp)
                    stack2.append((i,building[i]))
                    break
            if stack2 == []:
                stack2.append((i,building[i]))
                result2.append(0)
                #print('//',stack,result)
    #print(result2)
    print(max(max(result),max(result2)))
    return max(max(result),max(result2))
lazer([8,4,7,8,10,2,9,7,8,12])
