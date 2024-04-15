import sys

# 입력 받기
n, m = map(int, input().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

# 단어의 길이와 출현 빈도를 저장할 딕셔너리 생성
word_counts = {}

# 각 단어의 길이와 출현 빈도를 계산하여 딕셔너리에 저장
for word in words:
    if len(word) >= m:
        word_counts[word] = word_counts.get(word, 0) + 1

# 정렬 기준에 맞게 정렬
sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for word, count in sorted_words:
    print(word)
