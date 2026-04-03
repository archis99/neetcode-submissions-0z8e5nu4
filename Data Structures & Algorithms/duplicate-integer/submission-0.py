class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for num in nums:
            vals.add(num)
        
        return len(nums) != len(vals)
        

        