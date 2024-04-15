import sys
from collections import Counter

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

# M 글자 이상인 단어만 필터링
words = [word for word in words if len(word) >= M]

# 단어의 빈도수 계산
word_counts = Counter(words)

# 조건에 맞게 정렬: 빈도수 내림차순, 길이 내림차순, 알파벳 사전순
sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], -len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)
