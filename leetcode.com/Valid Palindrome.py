"""
https://leetcode.com/problems/valid-palindrome/
Valid Palindrome
"""


class Solution:
    alphanumeric = 'qwertyuiopasdfghjklzxcvbnm1234567890'

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = []
        for ch in s:
            if ch in self.alphanumeric:
                result.append(ch)

        if result == result[::-1]:
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # make sentence lower.
        s = ''.join(filter(str.isalnum, s))  # remove non-alphanumeric chars in sentence.

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


s = Solution()

print(s.isPalindrome("0P") == False)
print(s.isPalindrome("a") == True)
print(s.isPalindrome("A man, a plan, a canal: Panama") == True)
print(s.isPalindrome("race a car") == False)
print(s.isPalindrome(" ") == True)
