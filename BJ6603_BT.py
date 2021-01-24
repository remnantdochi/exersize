import sys

def BT(lotto, lotto_array, index):
    #print(lotto,index)
    if len(lotto) == 6 :
        print(" ".join(lotto))
        return
    if index<len(lotto_array):
        lotto.append(lotto_array[index])
        BT(lotto,lotto_array,index+1)
        lotto.pop()
        BT(lotto,lotto_array,index+1)

while(1):

    lotto_array = list(map(str, sys.stdin.readline().split()))
    if len(lotto_array) == 1: break
    K = lotto_array[0]
    lotto = []
    BT(lotto, lotto_array[1:],0)
    print()
