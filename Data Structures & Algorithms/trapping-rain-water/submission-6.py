class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)
        l, r = 0, len(height) - 1
        if len(height) < 3:
            return sum(water)
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = height[0]
        suffix[len(height)-1] = height[len(height)-1]
        max_pre = height[0]
        max_suf = height[len(height)-1]
        for i in range(1, len(height)):
            max_pre = max(max_pre, height[i-1])
            prefix[i] = max_pre
            max_suf = max(max_suf, height[-i])
            suffix[-i-1] = max_suf
        
        for i in range(1, len(height) - 1):
            level = min(prefix[i], suffix[i])
            if height[i] <= level:
                water[i] = level - height[i]
        
        return sum(water)