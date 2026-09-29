class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        if len(dup) == len(nums):
            return False
        return True