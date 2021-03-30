def solution(msg):
    
    dic = {}
    
    for i in range(1, 27):
        dic[chr(ord('A')+i-1)] = i

    w = 0
    c = 1

    answer = []

    while w < len(msg):
        while dic.get(msg[w:c]) is not None and c <= len(msg):
            c += 1
        answer.append(dic.get(msg[w:c-1]))
        dic[msg[w:c]] = len(dic)+1
        w = c-1
        c = w+1
        
    return answer