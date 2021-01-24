from itertools import permutations #순열 함수

N = int(input())
N_list = [i for i in range(1, N+1)]

for numbers in list(permutations(N_list)):
    for num in numbers:
        print(num, end=' ')
    print()


def BT(numbers):
    if len(numbers) == N :
        for item in numbers : print(item, end = " ")
        print()
        return
    for i in range(1,N+1):
        if i not in numbers:
            numbers.append(i)
            BT(numbers)
            numbers.pop()

BT([])
