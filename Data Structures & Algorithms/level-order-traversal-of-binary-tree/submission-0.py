# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([])
        if not root:
            return []
        output = [[root.val]]
        q.append(root)

        while q:
            temp = []
            while q:
                node = q.popleft()
                temp.append(node.left)
                temp.append(node.right)
            temp1 = []
            for i in temp:
                if i:
                    q.append(i)
                    temp1.append(i.val)
            if temp1:
                output.append(temp1)
        
        return output

