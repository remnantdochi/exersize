def beautifulArray(N):
    """
    :type N: int
    :rtype: List[int]
    """
    dp = [list(range(1, i+1)) for i in range(N+1)]
    print(N)
    print(dp)
    for i in range(2, N+1):
        for j in range(i):
            candidate = [ele for ele in dp[i-1]]
            print('1',candidate)
            candidate.insert(j, i)
            print('2',candidate)
            if check(candidate, j, i):
                dp[i] = candidate
                break

    return dp[N]

def check(candidate, idx, val):
    for i, ele in enumerate(candidate):
        if i == idx:
            continue
        start, end = (i, idx) if i < idx else (idx, i)
        for k in range(start+1, end):
            if 2 * candidate[k] == ele + val:
                return False
    return True
print(beautifulArray(3))
print(beautifulArray(4))
print(beautifulArray(5))
print(beautifulArray(6))
