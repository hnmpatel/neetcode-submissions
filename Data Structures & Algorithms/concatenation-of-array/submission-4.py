class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    def getConcatenation_1(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        i = 0
        while i < 2*l:
            index = i
            if i >= l:
                index = i - l
            ans.append(nums[index])
            i += 1
        return ans