class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            

"""
if target > nums[r] then search left sorted
if target < nums[l] then search right sorted

l < target < m - search left, r = m - 1
l < target > m  - search left, r = m - 1
l < target > m but l < m - search right, l = m + 1

l > target < m - search right, l = m + 1
l > target > m - search right, l = m + 1
l > target < m but l > m - search left, r = m - 1

before that, check if m = target
"""


