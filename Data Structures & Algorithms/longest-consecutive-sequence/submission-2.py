class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_dict = {}
        nums = set(nums)

        for i in nums:
            if i not in seq_dict and i-1 not in nums:
                seq_dict[i] = []
        
        maxest = 0
        
        for i in seq_dict:
            temp = i
            maxz = 1
            while temp+1 in nums:
                temp+=1
                maxz+=1
            maxest = max(maxz, maxest)

        return maxest
