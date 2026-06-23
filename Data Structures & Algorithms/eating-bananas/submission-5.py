import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while(l<=r):
            sumz = 0
            mid = l + (r-l)//2

            for i in piles:
                sumz+=math.ceil(i/mid)
            if(sumz<=h):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
                
        return res