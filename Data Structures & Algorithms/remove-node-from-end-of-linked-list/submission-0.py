# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. count nodes
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        # 2. Dummy gives the head a previous node
        dummy = ListNode(0,head)

        # 3. Find the node before the target
        prev = dummy

        for _ in range(length - n):
            prev = prev.next

        # 4. skip the target
        prev.next = prev.next.next

        return dummy.next
        # Time complexity - O(n)
        # Space complexity - O(1)