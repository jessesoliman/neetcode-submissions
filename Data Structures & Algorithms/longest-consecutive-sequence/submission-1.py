class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        starts = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
        for num in num_set:
            if num - 1 in num_set:
                continue
            starts.add(num)

        length = 0
        while len(starts) > 0:
            to_rm = set()
            for num in starts:
                if num + length in num_set:
                    continue
                else:
                    to_rm.add(num)
            starts.difference_update(to_rm)
            if len(starts) > 0:
                length += 1
        
        return length
        
