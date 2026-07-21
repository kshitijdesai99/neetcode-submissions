# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return True
        def isSame(leftTree, rightTree):
            if not leftTree and not rightTree:
                return True
            elif (leftTree and rightTree) and (leftTree.val != rightTree.val):
                return False
            elif (leftTree and not rightTree) or (rightTree and not leftTree):
                return False
            else:
                return (isSame(leftTree.left, rightTree.left)
                and isSame(leftTree.right, rightTree.right))
            return False
        return(
            isSame(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

        # Time complexity - O(mn)
        # Space complexity - O(m+n)