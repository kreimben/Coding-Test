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


s = Solution()

print(s.isPalindrome("0P") == False)
print(s.isPalindrome("a") == True)
print(s.isPalindrome("A man, a plan, a canal: Panama") == True)
print(s.isPalindrome("race a car") == False)
print(s.isPalindrome(" ") == True)
