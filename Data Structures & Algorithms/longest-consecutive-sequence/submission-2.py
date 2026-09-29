class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = set()

        # i don't need to do this portion if i just keep track of longest sequence
        # iterate through and find the starts

        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                next_num = num + 1
                length = 1
                while next_num in num_set:
                    next_num += 1
                    length += 1
                longest = max(longest, length)
        return longest

        
