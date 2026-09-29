class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero_count += 1
                if zero_count >= 2:
                    return [0] * len(nums)
        if zero_count == 0:
            return [prod//num for num in nums]
        else:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(prod)
        return res