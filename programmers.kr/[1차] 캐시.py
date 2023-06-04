"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
[1차] 캐시
"""


def solution(cache_size: int, cities: [str]) -> int:
    cities = [city.lower() for city in cities]

    class Element:
        def __init__(self, city_index: int, city_name: str):
            self.index: int = city_index
            self.city: str = city_name

        def __str__(self):
            return f'{self.city} ({self.index})'

    cache: [Element] = []
    time = 0

    for index, city in enumerate(cities):
        is_hitted = False
        for element in cache:
            if element.city == city:
                time += 1
                is_hitted = True
                element.index = index
                break

        if is_hitted:
            continue

        if cache_size == 0:
            ...
        elif len(cache) >= cache_size:
            m = min([e.index for e in cache])
            min_index = 0
            for i, element in enumerate(cache):
                if m == element.index:
                    min_index = i
                    break
            cache[min_index] = Element(index, city)
        else:
            cache.append(Element(index, city))
        time += 5

    return time


assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
assert solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                    "NewYork", "Rome"]) == 60
assert solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                    "NewYork", "Rome"]) == 52
assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
