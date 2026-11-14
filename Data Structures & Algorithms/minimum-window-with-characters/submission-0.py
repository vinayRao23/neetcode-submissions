from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        window = {}
        
        have = 0
        left = 0
        need = len(countT)
        curr_substring = ""

        result, resultLength = [-1, -1], float('infinity')

        for right in range(len(s)):
            val = s[right]
            window[val] = 1 + window.get(val, 0)

            if val in countT and window[val] == countT[val]:
                have += 1
            
            while have == need:
                if (right-left) + 1 < resultLength:
                    result = [left, right]
                    resultLength = right-left+1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        left, right = result

        return s[left:right+1] if resultLength != float("infinity") else ""



