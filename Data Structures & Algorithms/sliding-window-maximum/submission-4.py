class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        heapq.heapify(max_heap)
        for i in range(len(nums)):
            if len(max_heap) < k - 1:
                heapq.heappush(max_heap, [-nums[i], i])
                continue
            heapq.heappush(max_heap, [-nums[i], i])
            maximum = max_heap[0]
            print(max_heap)
            res.append(-maximum[0])
            if maximum[1] <= i-k+1:
                heapq.heappop(max_heap)
                if len(max_heap)>0:
                    duplicate = max_heap[0]
                    while duplicate[1] <= i-k + 1 and duplicate[0] == maximum[0]:
                        heapq.heappop(max_heap)
                        duplicate = max_heap[0]
        return res
