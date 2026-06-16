class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxy = float('-inf')

        while(i<j):
            area = min(heights[i],heights[j])*(j-i)
            maxy = max(area, maxy)
            if(heights[i]<=heights[j]):
                i+=1
            else:
                j-=1
        
        return maxy