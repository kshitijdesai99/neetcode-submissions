class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        output = nums[l]

        while(l<=r):
            mid = l + (r-l)//2
            print(mid)
            if(nums[mid]>=nums[l]):
                output = min(output, nums[l])
                l = mid + 1
            else:
                output = min(output, nums[mid])
                r = mid - 1


        return output