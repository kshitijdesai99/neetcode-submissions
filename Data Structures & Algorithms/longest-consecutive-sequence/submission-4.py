class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_set = set()
        nums = set(nums)

        for i in nums:
            if i not in seq_set and i-1 not in nums:
                seq_set.add(i)
        
        maxest = 0
        
        for i in seq_set:
            temp = i
            maxz = 1
            while temp+1 in nums:
                temp+=1
                maxz+=1
            maxest = max(maxz, maxest)

        return maxest
