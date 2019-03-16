N=int(input())
heights=[]
for i in range(N):
    heights.append(int(input()))

top=[0,heights[0]]
stack=[[0,heights[0]]]
result1=[0]
for i in range(1,N):
    temp=stack.pop()
    #print('test1',stack,i,temp)
    '''if stack == []:
        stack.append([i,heights[i]])
        result1.append(0)
        continue'''
    if heights[i] < temp[1]:
        result1.append(i-temp[0])
        stack.append(temp)
        stack.append([i,heights[i]])
        #print('test2',stack,i,temp)
    else:
        #print('test3',stack,i,temp)
        if stack==[]:
            stack.append([i,heights[i]])
            result1.append(0)
            continue
        temp=stack.pop()
        if stack==[]:
            if heights[i] <temp[1]:
                result1.append(i-temp[0])
                stack.append(temp)
                stack.append([i,heights[i]])
            else:
                stack.append([i,heights[i]])
                if temp[1]==heights[i]:
                    result1.append(i-temp[0])
                else: result1.append(0)
            #print('test4',stack,i,temp)
            continue
        while stack != []:
            #print('test5',stack,i,temp)
            if heights[i] < temp[1]:
                result1.append(i-temp[0])
                stack.append(temp)
                stack.append([i,heights[i]])
                #print('test2',stack,i)
                break
            else:
                stack.append([i,heights[i]])
                if temp[1]==heights[i]:
                    result1.append(i-temp[0])
                #print('test3',stack,i,result1)
                break
stack=[[N-1,heights[N-1]]]
result2=[0]
for i in range(N-2,-1,-1):
    temp=stack.pop()
    print('test1',stack,i,temp)
    '''if stack == []:
        stack.append([i,heights[i]])
        result1.append(0)
        continue'''
    if heights[i] > temp[1]:
        result2.append(temp[0]-i)
        print('#',temp[0]-i)
        stack.append(temp)
        stack.append([i,heights[i]])
        print('test2',stack,i,temp)
    else:
        print('test3',stack,i,temp)
        if stack==[]:
            stack.append([i,heights[i]])
            result2.append(0)
            continue
        '''
        temp=stack.pop()
        if stack==[]:
            if heights[i] <temp[1]:
                result2.append(temp[0]-i)
                stack.append(temp)
                stack.append([i,heights[i]])
            else:
                stack.append([i,heights[i]])
                if temp[1]==heights[i]:
                    result2.append(temp[0]-i)
                else: result2.append(0)
            print('test4',stack,i,temp)
            continue'''
        while stack != []:
            temp=stack.pop()
            print('test5',stack,i,temp)
            if heights[i] > temp[1]:
                result2.append(temp[0]-i)
                stack.append(temp)
                stack.append([i,heights[i]])
                print('test6',stack,i)
                break
            else:
                stack.append([i,heights[i]])
                if temp[1]==heights[i]:
                    result2.append(temp[0]-i)
                    print('test7',stack,i,result1)
                    break


print(result1)
print(result2)
print(max(max(result1),max(result2)))
