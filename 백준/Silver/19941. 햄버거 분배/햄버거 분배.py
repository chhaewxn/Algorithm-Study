# 선택거리 K 이하의 왼쪽에 위치한 햄버거 먹기 
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 테이블 크기는 N, 선택 거리는 K 이하
S = input().rstrip() 
table_list = list(S)
count = 0

for i in range(len(table_list)):
  if table_list[i] == "P":
    for j in range(i-K, i+K+1):
      if 0 <= j < N and table_list[j] == "H":
        count += 1
        table_list[j] = "E"
        break

print(count)
