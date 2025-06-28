def solution(numbers, hand):
    key_pos = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        '*': (3,0), 0: (3,1), '#': (3,2)
    }

    left_pos = key_pos['*']
    right_pos = key_pos['#']
    
    result = ''
    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left_pos = key_pos[num]
        elif num in [3, 6, 9]:
            result += 'R'
            right_pos = key_pos[num]
        else:  
            target_pos = key_pos[num]
            l_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            r_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
            
            if l_dist < r_dist:
                result += 'L'
                left_pos = target_pos
            elif r_dist < l_dist:
                result += 'R'
                right_pos = target_pos
            else:
                if hand == 'right':
                    result += 'R'
                    right_pos = target_pos
                else:
                    result += 'L'
                    left_pos = target_pos
    return result
