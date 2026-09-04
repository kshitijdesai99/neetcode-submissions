# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        temp = l3
        carry = 0
        total = 0
        while l1 or l2:
            if l2:
               total += l2.val
               l2 = l2.next
            if l1:
                total += l1.val
                l1 = l1.next
            total += carry
            carry = total // 10
            digit = total % 10
            temp.next = ListNode(digit)
            temp = temp.next
            total = 0
        if carry!=0:
            temp.next = ListNode(carry)
        return l3.next
