class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def search(curr):
            if len(curr)==len(nums):
                nonlocal result
                result.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                curr.append(nums[i])
                used.add(nums[i])
                search(
                    curr = curr
                )
                curr.pop()
                used.remove(nums[i])

        search(
            curr = []
        )
        # Space comlexity - O(n)
        # Time complexity - O(n*n!)
        return result