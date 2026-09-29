class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()

        for i in range(1, len(nums)):
            val = nums[i] * prefix[i-1]
            prefix[i] = val
            val_suf = nums[-i-1] * suffix[-i]
            suffix[-i-1] = val_suf
            print(prefix, suffix)
        
        res = [suffix[1]]

        for i in range(1, len(nums)-1):
            res.append(prefix[i-1] * suffix [i+1])

        res.append(prefix[-2])
        return res