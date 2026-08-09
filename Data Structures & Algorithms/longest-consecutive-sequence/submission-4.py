class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        u_nums = sorted(list(set(nums)))
        longest = 1
        counter = 1
        for i, n in enumerate(u_nums):
            if i == 0:
                continue
            prev = u_nums[i-1]
            if n - prev == 1:
                counter += 1
                longest = max(longest, counter)
            else:
                counter = 1
        return longest
