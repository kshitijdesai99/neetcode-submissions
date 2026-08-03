# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        if root is not None:
            curMax = root.val
        def dfs(node, max_so_far):
            nonlocal count
            if node == None:
                return 
            if node.val>=max_so_far:
                count+=1
            max_so_far = max(max_so_far, node.val)
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)

        dfs(root, root.val)
        # Time complexity - O(n)
        # Space complexity - O(n)
        return count