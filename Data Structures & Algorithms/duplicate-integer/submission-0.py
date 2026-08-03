class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = []
        for n in nums:
            if n in hash_map:
                return True
            hash_map.append(n)
        return False
                
            
        