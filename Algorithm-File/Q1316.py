def is_group_word(word):
    seen = set()  # 이미 나온 문자를 저장할 set
    prev = ''     # 이전 문자를 저장할 변수
    
    for char in word:
        if char != prev:  # 현재 문자가 이전 문자와 다르면
            if char in seen:  # 이미 나온 문자인지 확인
                return False
            seen.add(char)    # 새로운 문자를 set에 추가
        prev = char
    
    return True

# 입력 받기
n = int(input())
count = 0

# n개의 단어에 대해 그룹 단어 검사
for _ in range(n):
    word = input()
    if is_group_word(word):
        count += 1

print(count)
