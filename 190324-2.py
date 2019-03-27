def wordbreak(s,wordDict):
    def wordsolution(particle):
        print(particle,'test')
        if particle=="": return True
        for word in wordDict:
            print('test2',word,particle)
            if word in particle:
                point=particle.index(word)
                print(particle[point+len(word):])
                return wordsolution(particle[point+len(word):])
        return False
    return wordsolution(s)
print(wordbreak("catsandog",  ["cats", "dog", "sand", "and", "cat"]))
