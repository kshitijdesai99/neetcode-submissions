class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output^=i
        return output
        # Time - O(n)
        # Space - O(1)