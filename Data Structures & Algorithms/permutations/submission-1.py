class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def search(curr):
            if len(curr)==len(nums):
                nonlocal result
                result.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if len(curr)>0 and nums[i] in curr:
                    continue
                curr.append(nums[i])
                search(
                    curr = curr
                )
                curr.pop()

        search(
            curr = []
        )
        return result