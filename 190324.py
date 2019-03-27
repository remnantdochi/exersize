def wordbreak(s,wordnote):
    changes=list(s)
    for word in wordnote:
        while word in s:
            print(word,changes)
            point=s.index(word)
            print(point)
            for i in range(len(word)):
                del changes[point]
            s=''.join(changes)
            print(s,changes)
    if changes==[]: return True
    else: return False
print(wordbreak("applepenapple",["apple", "pen"]))
