# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of list to reverse
        prev = slow.next = None # break the list now

        # reverse the list
        while second:
            tmp = second.next # store next (will become new prev)
            second.next = prev
            prev = second
            second = tmp

        # we have a reversed second half now we need to merge them back
        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2