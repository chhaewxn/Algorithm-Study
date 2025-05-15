def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    total_time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            total_time += 5
            if len(cache) >= cacheSize:
                cache.pop(0)  # 가장 오래된 것 제거
            cache.append(city)
    
    return total_time