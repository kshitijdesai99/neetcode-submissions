class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = l + (r-l)//2  # 0 + (5-0)//2 -> 2
            if(nums[mid]>target): # 2 > 4
                r = mid - 1
            elif(nums[mid]<target): # 2 < 4
                l = mid + 1
            else:
                return mid
        return -1