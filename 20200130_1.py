def sol(A):
    for item in A:
        total = []
        temp = set()
        for i in item:
            temp.append(ord(i))
        print(temp)
        if len(temp) == len(item):
            total.append(temp)
        print(total)

#sol("abca")
print("abc")
