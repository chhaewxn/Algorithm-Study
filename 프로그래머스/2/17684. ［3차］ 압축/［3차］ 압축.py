def solution(msg):
    dictionary = {chr(i + 64): i for i in range(1, 27)}  
    
    next_index = 27
    result = []
    
    i = 0
    
    while i < len(msg):
        w = msg[i]
        j = i + 1
        
        while j < len(msg) and w + msg[j] in dictionary:
            w += msg[j]
            j += 1
        
        result.append(dictionary[w])
        
        # 사전에 없는 새로운 문자열 등록
        if j < len(msg):
            dictionary[w + msg[j]] = next_index
            next_index += 1

        i += len(w)
    
    return result