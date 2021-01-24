def solution(emails):
    answer = 0
    for item in emails:
        i1 = item.find('@')
        print('i1',i1)
        if i1 == -1: continue
        name = ''.join(item[:i1])
        if name.lower() != name:
            print(name.lower())
            print(item[:i1])
            print('test1')
            continue
        if '@' in item[i1+1:]:
            print('test2')
            continue

        i2 = item[i1+1:].find('.')
        if i2 == -1: continue
        print(item[i2+i1+1:])
        if item[i2+i1+1:] == 'com' or item[i2+2+len(name):] != 'net' and item[i2+2+len(name):] != 'org':
            print('test3')
            print(item[i2+2+len(name):] != 'com')
            domain = ''.join(item[i2+1+len(name):])
            print(domain)
            print(domain != 'com')
            continue
        answer +=1
    return answer
print(solution(["a@abc.com"]))
