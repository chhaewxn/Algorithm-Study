def solution(arr):
    def compress(x, y, size):
        first_value = arr[x][y]
        
        all_same = True
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first_value:
                    all_same = False
                    break
            if not all_same:
                break
        
        if all_same:
            if first_value == 0:
                result[0] += 1  # 0개수 증가
            else:
                result[1] += 1  # 1개수 증가
        else:
            half_size = size // 2
            compress(x, y, half_size)                          
            compress(x, y + half_size, half_size)      
            compress(x + half_size, y, half_size)            
            compress(x + half_size, y + half_size, half_size)  

    result = [0, 0]
    compress(0, 0, len(arr))
    
    return result