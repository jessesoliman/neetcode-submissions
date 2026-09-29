class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            comp = -(nums[i])
            j, k = i + 1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == comp and tuple([nums[i], nums[j], nums[k]]) not in res:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                elif nums[j] + nums[k] > comp:
                    k -= 1
                else:
                    j += 1
        
        return [item for item in res]
