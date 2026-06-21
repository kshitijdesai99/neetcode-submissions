class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair (i,h)

        for i,h in enumerate(heights):
            start = i
            while(stack and stack[-1][1]>h):
                i_1, h_1 = stack.pop()
                max_area = max(max_area, h_1 * (i - i_1))
                start = i_1
            stack.append([start,h])

        for i,h in stack:
            max_area = max(max_area, h * (len(heights)-i))

        return max_area