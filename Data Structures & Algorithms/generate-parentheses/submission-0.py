class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def search(curr = [], right = n, left = n):
            if right==0 and left == 0:
                result.append("".join(curr))
                return

            # Use an operating parenthesis
            if left > 0:
                curr.append("(")
                search(curr, right, left - 1)
                curr.pop()

            # Use a closing parenthesis
            if right > left:
                curr.append(")")
                search(curr, right - 1, left)
                curr.pop()
                
        search()
        # Time complexity - O(4^n/sqrt(n))
        # Space complexity - O(n)

        return result