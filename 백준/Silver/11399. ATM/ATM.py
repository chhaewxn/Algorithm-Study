def solution(times):
    times.sort()
    prev = 0
    answer = 0 
    
    for t in times : 
        prev += t
        answer += prev    
    return answer

if __name__ == "__main__" :
    n = int(input())
    times = list(map(int, input().split()))
    print(solution(times))