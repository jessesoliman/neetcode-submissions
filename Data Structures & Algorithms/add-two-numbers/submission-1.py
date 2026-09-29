# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        list1 = l1
        list2 = l2
        dummy = ListNode(0)
        total = dummy

        prev = None
        while list1 and list2:
            if prev:
                prev = total
            in_place = remainder + list1.val + list2.val
            if in_place > 9:
                total.val = in_place - 10
                remainder = 1
            else:
                total.val = in_place
                remainder = 0
            list1 = list1.next
            list2 = list2.next
            total.next = ListNode(0)
            prev = total
            total = total.next
        print(prev.val)
        if list1:
            while list1:
                in_place = remainder + list1.val
                if in_place > 9:
                    total.val = in_place - 10
                    remainder = 1
                else:
                    total.val = in_place
                    remainder = 0
                total.next = ListNode(0)
                prev = total
                total = total.next
                list1 = list1.next
        elif list2:
            while list2:
                in_place = remainder + list2.val
                if in_place > 9:
                    total.val = in_place - 10
                    remainder = 1
                else:
                    total.val = in_place
                    remainder = 0
                total.next = ListNode(0)
                prev = total
                total = total.next
                list2 = list2.next
        if remainder == 1:
            total.val = 1
            total.next = None
        else:
            prev.next = None
        return dummy
