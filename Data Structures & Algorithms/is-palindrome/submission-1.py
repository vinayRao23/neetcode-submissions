class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        slow = 0
        fast = len(s) - 1

        for i in range(len(s)):
            if not s[fast].isalnum():
                fast -= 1
            elif not s[slow].isalnum():
                slow += 1
            elif s[slow] != s[fast]:
                return False
            else:
                slow += 1
                fast -= 1

        return True
            