class Solution:
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
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
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        res = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            res = max(res, right - left + 1)
        return res