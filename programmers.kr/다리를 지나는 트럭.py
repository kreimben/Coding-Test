"""
https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
다리를 지나는 트럭
"""

def solution(bridge_length, weight, truck_weights):
    time = 1
    passed_truck = []
    waiting_truck = truck_weights
    now_in_bridge = []
    front_bridge = 0
    back_bridge = 0

    while waiting_truck:
        now_in_bridge.append(waiting_truck[0])


