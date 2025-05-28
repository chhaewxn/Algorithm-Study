
def solution(numbers):
    sums = set()  # 중복 제거를 위한 집합
    
    # 서로 다른 인덱스의 모든 조합 시도
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.add(numbers[i] + numbers[j])
    
    # 집합을 리스트로 변환하고 오름차순 정렬
    return sorted(list(sums))