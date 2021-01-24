import itertools

L,C = map(int,input().split())

letter = sorted(list(map(str,input().split())))
vowel = ['a','e','i','o','u']

result = itertools.combinations(letter,L)
for item in result:
    cnt = 0
    for l in item:
        if l in vowel:
            cnt+=1
    if cnt>=1 and cnt<=L-2: print(''.join(item))
