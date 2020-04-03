N = int(input())

def BT(numbers):
    for i in range(1, len(numbers)//2+1):
        if numbers[-i*2:-i] == numbers[-i:]: return False

    if len(numbers) == N:
        ##일단 여기 도달하면 그게 최소임
        for item in numbers : print(item, end = "")
        return True

    for i in range(1,4):
        numbers.append(i)
        #print(numbers)
        if BT(numbers):
            numbers.pop()
            return True
        numbers.pop()

BT([])
