class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxest = 0

        for i in nums:
            if i-1 not in nums:
                temp = i
                maxz = 1
                while temp+1 in nums:
                    temp+=1
                    maxz+=1
                maxest = max(maxz, maxest)

        return maxest
