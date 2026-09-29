class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + nums[j] == target:
                return [i, j]
        return self.twoSum(nums[:j], target)
