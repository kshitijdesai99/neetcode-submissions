# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root,False)] # Node, children_visited

        if not stack:
            return True

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

        return True
