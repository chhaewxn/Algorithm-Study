def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    
    if total_sum % 2 == 1:
        return -1
    
    target = total_sum // 2
    n = len(queue1)
    
    arr = queue1 + queue2
    
    # queue1의 시작과 끝 인덱스
    left = 0  #
    right = n - 1 
    
    current_sum = sum(queue1)
    operations = 0

    max_operations = len(arr) * 2
    while operations <= max_operations:
        if current_sum == target:
            return operations
        
        # queue1의 합이 목표보다 큰 경우 queue1에서 pop
        elif current_sum > target:
            current_sum -= arr[left]
            left = (left + 1) % len(arr)  
            operations += 1
            
        # queue1의 합이 목표보다 작은 경우 queue2에서 pop해서 queue1에 추가
        else:
            right = (right + 1) % len(arr) 
            current_sum += arr[right]
            operations += 1
    
    return -1