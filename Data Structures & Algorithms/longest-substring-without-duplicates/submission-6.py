class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        counter = 0
        s_s = {}
        ss = ""
        for i in range(len(s)):
            if s[i] in ss:
                res = max(res, counter)
                ss = ss[ss.find(s[i]) + 1:] + s[i]
                counter = len(ss)
            else:
                ss += s[i]
                counter += 1                
        return max(res, counter)
            
