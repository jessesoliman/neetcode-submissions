# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        slow = dummy
        fast = head
        for i in range(n): # move fast pointer to the nth node
            if fast is None:
                return None
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        # remove nth node
        slow.next = slow.next.next
        return dummy.next
        

