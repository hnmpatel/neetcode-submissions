class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)   
        pre_prod = 1 
        suf_prod = 1
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            product[i] *= pre_prod
            product[j] *= suf_prod
            pre_prod *= nums[i]
            suf_prod *= nums[j]
        return product