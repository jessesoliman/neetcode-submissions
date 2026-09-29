class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = int()
        for i in range(1, len(numbers)):
            if numbers[0] + numbers[i] == target:
                return [1, i+1]
            if numbers[0] + numbers[i] > target:
                end = i - 1
        end = len(numbers) - 1
        
        start = 0

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            if numbers[start] + numbers [end] > target:
                end -= 1
            else:
                start += 1