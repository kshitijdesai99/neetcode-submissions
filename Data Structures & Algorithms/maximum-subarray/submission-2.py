class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_so_far = previous_sum = float("-inf")

        for i in nums:
            previous_sum += i
            previous_sum = max(previous_sum,i)
            best_so_far = max(best_so_far, previous_sum)
        
        # Time complexity - O(n)
        # Space complexity - O(1)

        return best_so_far