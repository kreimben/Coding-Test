"""
https://leetcode.com/problems/boats-to-save-people/description/
Boats to Save People
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        while people:
            last_person = people.pop()
            if people and last_person + people[0] <= limit:
                people.pop(0)
            count += 1
        return count
