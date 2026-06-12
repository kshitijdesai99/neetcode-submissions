class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1]*len(nums)
        for i in range(1,len(nums)):
            suffix[i] = suffix[i-1]*nums[i-1]

        prefix = [1]*len(nums)
        for i in range(len(nums)-2,-2,-1):
            prefix[i] = prefix[i+1]*nums[i+1]
            suffix[i+1] = suffix[i+1]*prefix[i+1]

        return suffix
