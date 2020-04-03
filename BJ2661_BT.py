N = int(input())
res = 3*(10**(N-1))
def possible(numbers):
    length = len(numbers)
    i=1
    while (length-2*i>=0):
        if (numbers[length-i*2:length-i] == numbers[length-i:]) : return False
        i= i*2
    return True

def BT(numbers):
    global res
    if len(numbers) == N:
        #print("".join(numbers))
        res = min(int("".join(numbers)), res)
        return
    for i in range(1,4):
        numbers.append(str(i))
        #print(numbers)
        if possible(numbers):
            BT(numbers)
            numbers.pop()
        else : numbers.pop()

BT([])
print(res)
