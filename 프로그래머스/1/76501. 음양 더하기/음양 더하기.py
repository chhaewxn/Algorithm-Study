def solution(absolutes, signs):
    total = 0
    
    for absolute, sign in zip(absolutes, signs):
        if sign:
            total += absolute  
        else:
            total -= absolute 
    
    return total