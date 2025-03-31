def solution(phone_book):
    # 전화번호를 정렬하면 접두어 관계에 있는 번호들이 인접하게 됨
    phone_book.sort()
    
    # 인접한 번호들을 비교하여 접두어 관계 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True