# 이곳에 소스코드를 작성하세요.
# Python3 만 지원됩니다.
T = int(input())
for num in range(1,T+1):
    N, K = map(int,input().split())
    papers = list(map(int,input().split()))
    checklist = [[0,0]]
    prev = papers[0]
    cnt = 0
    for item in papers:
        if item == prev:
            cnt+=1
            continue
        else:
            checklist.append([prev,cnt])
            cnt = 1
            prev = item
    checklist.append([prev,cnt])
    checklist.append([K+1,0])
    if len(checklist) == 3 :
        print("#{0} {1}".format(num,N-K+1))
        continue

    prev = checklist[0][0] #0
    cnt = checklist[0][1] #0
    for i in range(1, len(checklist)-1):
        item = checklist[i][0]
        if item != 0:
            sum = checklist[i][1]
            if checklist[i-1][0] == 0:
                sum += checklist[i-1][1] - (item-prev-1)
            if checklist[i+1][0] == 0:
                sum += checklist[i+1][1] - (checklist[i+2][0]-item-1)
            checklist[i][1] = sum
            prev = item

    maxlist = []
    for item in checklist:
        if item[0] != 0: maxlist.append(item[1])
    print("#{0} {1}".format(num,max(maxlist)))
