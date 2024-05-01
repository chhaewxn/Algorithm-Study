import sys

# 입력 받기
n, x = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))

# 초기 최대 방문자 수 및 그 기간 동안의 총 방문자 수 계산
max_sum = sum(visitors[:x])
current_sum = max_sum
count = 1

for i in range(x, n):
    # 현재 기간의 방문자 수 업데이트: 새로운 날짜 추가 및 가장 오래된 날짜 제거
    current_sum += visitors[i] - visitors[i-x]

    # 최대 방문자 수 갱신
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

# 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)
