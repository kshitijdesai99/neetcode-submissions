class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1

        max_suffix = []
        max_prefix = []

        maxy = float("-inf")
        for i in height:
            maxy = max(maxy, i)
            max_suffix.append(maxy)

        maxy = float("-inf")
        for i in height[::-1]:
            maxy = max(maxy, i)
            max_prefix.append(maxy)

        max_prefix = max_prefix[::-1]

        total = 0
        for i in range(len(height)):
            total+=min(max_prefix[i],max_suffix[i]) - height[i]

        return total

        
            
        
