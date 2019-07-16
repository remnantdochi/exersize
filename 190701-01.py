#T = int(input())
#for i in range(1,T+1):
N, K = map(int,input().split())
papers = list(map(int,input().split()))
counts = []
color = []
beforec= papers[0]
lenc = 1
##########여기까지 준비단계
for i in range(1,len(papers)):
    if papers[i] == beforec:
        lenc +=1
    else:
        color.append(papers[beforec])
        counts.append(lenc)
        lenc = 1
        beforec = papers[i]
if lenc != 1:
    color.append(papers[-1])
    counts.append(lenc)
##########판단
#일단은 첨이 0이 아니라는 가정
#가장 기본은 일단 0과 0사이의 숫를 볼지 숫자와 숫자 사이의 0을 볼지
#후자 선택 - 그럼 처음에 일단 0 이 아닌 처음 index부터 가르켜야함
#둘 중 하나겠지 첨이 0이던가 아니던가
#일단 0이 아닌 경우부터 시작
#그럼 그 다음을 봐서 0이면 판단안하고 저장만 해둔후
# 0이 아닌 숫자 나올때까지
# 이전 index랑 같은 숫자 - 중간 0 index에 값 포함 : '10101'
# : 아냐 그냥 color랑 count에서 제껴야할듯, 이것만 좍 해서 일단 정리
# 0이 젤 처음일 경우 그 다음이 1인 가정하에 먹힘
# 마찬가지로 제일 마지막일 경우에도 그 전이 0이 아닌 가정하에 먹힘
# 이건 아닌듯 그 전의 index가 k여야 함 그래야지 먹힘
# 아니면 후......
#후우 기준을 0으로 잡는다하자 dict 필요함^^
#0

# 일단 원칙은 뒤에 가서 정리해주는 걸로 ?? dict를 만들어야할까?
#   이전 index의 0의 여부를 판단해야겠네
# 그냥 나를 기준으로 판단해야겠네
# 내가 1일경우와 아닌 경우를 나누자. 내 다음에 0이 있는지를 봐서 더해
# 내가 1이 아닌 경우. 앗 단 내 이전 index와 나를 비교해야겠지
#   내 이전 index가 나랑 1 차이 나는 경우. 그냥 나의 앞뒤 0여부 추가
#   내 이전 index와 1 이상 차이 나는 경우. : 무조건 전에 0존재
#          0204이면 어케해 204와 다른건데
#   내 이전과 다음에 0이 있는지를 봐서 더해
# 이전 index에 1 더한 숫자 -
#    그 이전이 0인지 아닌지 판단
#       그 이전이 0: 이전 index의 값 + 0 의 값 더하기
#           '?1020'    그 다음이 0: 앞 뒤 더해서 poss에 추가
#           '?1023'       그 다음이 0이 아님:
#       0 아닐경우 : '12'이전 index의 count값 poss에 추가
#     이전 index의 값이 바뀜
#   지금 문제가 10204일지 10203일지 모르는건데
# 이전 index보다 1보다 큰 숫자 : 이건 반드시 사이 0이 있다

#maxlen = 0
startindex = 1
nowindex = 1
pastcolorindex = 0
pastcolor = color[0]
zeronum = 0
possible = []




for i in range(1,len(color)):
    if color[i] == 0:
        zeronum = counts[i]
        possible.append( counts[pastcolorindex] + zeronum )
    else if color[i] == pastcolor:
        print()
