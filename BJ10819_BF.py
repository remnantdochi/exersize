from collections import deque
import copy
N= int(input())
array = sorted(list(map(int,input().split())))
array = deque(array)
ans = deque()
array2 = copy.deepcopy(array)
ans2 = deque()

ans.append(array.pop())
ans.append(array.popleft())
ans.appendleft(array.popleft())

order = 1

while len(array) != 0:

    if order == 1: ans.append(array.pop())
    elif order == 2: ans.appendleft(array.pop())
    elif order == 3: ans.append(array.popleft())
    else:
        ans.appendleft(array.popleft())
        order = 1
        continue
    order +=1

sum=0
for i in range(1,N):
    sum+=abs(ans[i]-ans[i-1])

order =1
ans2.append(array2.popleft())
ans2.append(array2.pop())
ans2.appendleft(array2.pop())

while len(array2) != 0:

    if order == 1: ans2.append(array2.popleft())
    elif order == 2: ans2.appendleft(array2.popleft())
    elif order == 3: ans2.append(array2.pop())
    else:
        ans2.appendleft(array2.pop())
        order = 1
        continue
    order +=1

sum2=0
for i in range(1,N):
    sum2+=abs(ans2[i]-ans2[i-1])
sum = max(sum2,sum)
print(sum)
