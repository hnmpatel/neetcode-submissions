class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)   
        pre_prod = 1 
        for i in range(len(nums)):
            product[i] = pre_prod
            pre_prod *= nums[i]
        suf_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= suf_prod
            suf_prod *= nums[i]
        return product