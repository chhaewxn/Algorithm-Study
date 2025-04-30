def solution(n, words):
    used_words = set()
    
    used_words.add(words[0])
    last_char = words[0][-1]  # 첫 단어의 마지막 글자
    
    for i in range(1, len(words)):
        current_word = words[i]
        
        # 이전에 등장한 단어인지 또는 끝말잇기 규칙을 어겼는지
        if current_word in used_words or current_word[0] != last_char:
            # 탈락자 정보 계산
            person_number = (i % n) + 1 
            turn_number = (i // n) + 1    
            return [person_number, turn_number]
        
        # 단어 추가 및 마지막 글자 갱신
        used_words.add(current_word)
        last_char = current_word[-1]
    
    return [0, 0]
