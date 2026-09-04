"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1 - 1st pass
        temp = head
        dummy = Node(0)
        dummy_copy1 = dummy
        id_map = {}
        while temp:
            dummy_copy1.next = Node(temp.val)
            id_map[temp] = dummy_copy1.next
            temp = temp.next
            dummy_copy1 = dummy_copy1.next

        # Step 2 - 2nd pass
        dummy_copy2 = dummy
        while head:
            if head.random == None:
                dummy_copy2.next.random = dummy_copy1.next
            else:
                dummy_copy2.next.random = id_map[head.random]
            head = head.next
            dummy_copy2 = dummy_copy2.next

        return dummy.next
        # Time complexity - O(n)
        # Space compexity - O(n)