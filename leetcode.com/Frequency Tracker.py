"""
https://leetcode.com/problems/frequency-tracker/
Frequency Tracker
"""


class FrequencyTracker:

    def __init__(self):
        self.cache = [0 for _ in range(10 ** 5 + 1)]
        self.s = {}

    def add(self, number: int) -> None:
        pre = self.cache[number]
        self.cache[number] += 1
        if pre not in self.cache:
            self.s[pre] = False
        self.s[self.cache[number]] = True

    def deleteOne(self, number: int) -> None:
        pre = self.cache[number]
        self.cache[number] -= 1
        if self.cache[number] < 0:
            self.cache[number] = 0
        if pre not in self.cache:
            self.s[pre] = False
        self.s[self.cache[number]] = True

    def hasFrequency(self, frequency: int) -> bool:
        return self.s.get(frequency, False)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
