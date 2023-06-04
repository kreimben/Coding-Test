"""
https://leetcode.com/problems/design-browser-history/
Design Browser History
"""
from collections import deque
from itertools import islice


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.history.append(homepage)
        self.index = 1

    def visit(self, url: str) -> None:
        self.history = deque(islice(self.history, 0, self.index + 1))
        self.history.append(url)
        self.index = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index += steps
        if self.index >= len(self.history):
            self.index = len(self.history) - 1
        return self.history[self.index]

# youtube
# facebook
# google

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
