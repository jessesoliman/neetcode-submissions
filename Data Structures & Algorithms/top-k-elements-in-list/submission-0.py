class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        freq = [[]for i in range(len(nums)+1)]
        print(freq)
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        # populate freq with numbers based on frequency
        # only indices 1 through len(nums) will have numbers
        for num, count in num_freq.items():
            freq[count].append(num)
        print(freq)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
