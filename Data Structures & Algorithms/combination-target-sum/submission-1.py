class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def search(start, curr, remaining):
            if remaining == 0:
                nonlocal result
                result.append(curr.copy())
                return

            if remaining<0:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                search(
                    start = i,
                    curr = curr,
                    remaining = remaining - nums[i]
                )
                curr.pop()


        search(
            start = 0,
            curr = [],
            remaining = target
        )

        # Time complexity - O(2^(t/m))
        # Space complexity - O(t/m)

        return result