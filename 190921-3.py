def solution(data):
    answer = []
    que = []
    remain = data[:]
    time = data[0][1]
    while remain != []:
        que.append(remain.pop(0))
        while que != []:
            que.sort(key=lambda x:x[2])
            now = que.pop(0)
            print('now',now)
            answer.append(now[0])
            time += now[2]
            cnt = 0
            print('time',time)
            for item in remain:
                if item[1] <= time:
                    cnt +=1
                    que.append(item)
                else : break
            print('q',que)

            if cnt != 0 : remain = remain[cnt:]
            print('r',remain)

    print(answer)
    return answer
solution([[1,2,10],[2,5,8],[3,6,9],[4,20,6],[5,25,5]])
