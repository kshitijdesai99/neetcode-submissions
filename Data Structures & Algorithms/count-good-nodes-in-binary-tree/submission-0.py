# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        temp = []
        count = 0
        if root is not None:
            count = 1
        def dfs(node):
            nonlocal count
            if node == None:
                return 
            if len(temp)!=0:
                if node.val>=max(temp):
                    count+=1
            temp.append(node.val)
            dfs(node.left)
            dfs(node.right)
            temp.pop()

        dfs(root)
        return count