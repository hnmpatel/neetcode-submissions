class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [x.lower() for x in s if x.isalnum()] == [x.lower() for x in s[::-1] if x.isalnum()]
        