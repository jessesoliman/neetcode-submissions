class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums) // 2
        l = 0
        r = len(nums) - 1
        if nums[0] > target > nums[-1]:
            return -1
        while nums[middle] != target:
            if (r == middle or l == middle) and nums[r] != target and nums[l] != target:
                return -1
            if target > nums[middle]:
                l = middle
                middle = middle + (-(-(r - l) // 2))
            else:
                r = middle
                middle = middle - (-(-(r - l) // 2))
        return middle


# 0, 1, 4, 8, 11, 15, 21 targ = 10