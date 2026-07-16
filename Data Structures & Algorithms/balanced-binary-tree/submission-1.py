# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root,False)] # Node, children_visited        

        height_map = {}

        while stack:
            node, is_visited = stack.pop()

            if not node:
                continue

            if not is_visited:         
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left_height = height_map.get(node.left,0)
                right_height = height_map.get(node.right,0)
                if(abs(left_height - right_height)>1):
                    return False
                height_map[node] = max(left_height, right_height) + 1

        # Time complexity - O(n)
        # Space complexity - O(n)

        return True
