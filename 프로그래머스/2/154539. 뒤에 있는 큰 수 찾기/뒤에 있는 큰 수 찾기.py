def solution(numbers):
    answer = [-1] * len(numbers)  # 기본값 -1
    stack = []  # 인덱스를 저장

    for i in range(len(numbers) - 1, -1, -1):  # 뒤에서부터 순회
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()  # 현재 수보다 작거나 같은 건 제거
        if stack:
            answer[i] = numbers[stack[-1]]  # 뒷 큰수 기록
        stack.append(i)  # 현재 인덱스를 스택에 넣음

    return answer
