class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        
        if nums[0] in nums[1:]:
            return True
        
        return self.hasDuplicate(nums[1:])