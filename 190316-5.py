def letterCasePermutation(S) :
        check=[0]*len(S)
        results=[]
        def makelist(index,result):
            if index==len(S):
                results.append(result)
                return results
            print(index,result)

            if S[index].isdigit():
                result.append(S[index])
                makelist(index+1,result)
            else:
                if check[index] == 0:
                    result.append(S[index].lower())
                    check[index] = 1
                    makelist(index+1,result)
                result.append(S[index].upper())
                check[index] = 0
                makelist(index+1,result)
        makelist(0,[])
        print(results)
letterCasePermutation('a1b2')
