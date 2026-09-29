class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amt = 0
        i, j = 0, len(heights) - 1
        while i < j:
            # check against tallest
            # 
            amt = max(amt, min(heights[i], heights[j]) * (j - i))
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
            else:
                i += 1
                j -= 1
        return amt
                