def solution(cacheSize, cities):
    time = 0
    cache = {}
    if cacheSize == 0:
         return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city not in cache.keys():
            # print(time)
            # print(city)
            # print(cache)
            if len(cache) < cacheSize:
                cache[city] = 0
            else:
                min_ref_city = list(filter(lambda x: x[1] == max(cache.values()), cache.items()))[0][0]
                # print(cache)
                # print('??', min_ref_city)
                cache.pop(min_ref_city)
                # print('??')
                # print(cache)
                cache[city] = 1
            
            time += 5
        else:
            cache[city] = 1
            time += 1
        
        for cityname in cache.keys():
            cache[cityname] += 1
        # print(cache)
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))