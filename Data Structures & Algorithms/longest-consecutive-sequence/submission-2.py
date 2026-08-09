class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        u_nums = sorted(list(set(nums)))
        longest = 0
        counter = 0
        streak = []
        for n in u_nums:
            if len(streak) == 0:
                streak.append(n)
                counter = 1
                longest = 1
                continue
            prev = streak[-1]
            if n - prev == 1:
                counter += 1
                streak.append(n)
                if counter > longest:
                    longest = counter
            else:
                streak = [n]
                counter = 1
        return longest
