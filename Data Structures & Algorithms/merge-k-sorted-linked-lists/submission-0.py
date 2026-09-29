# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))

        dummy = tail = ListNode(0)

        while minheap:
            _, i, node = heapq.heappop(minheap)

            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))

        return dummy.next