class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result  = []
        nums.sort()
        def search(start, remaining, current):
            nonlocal result
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start,len(nums)):
                choice = nums[i]

                if choice > remaining:
                    break

                # move forward
                current.append(choice)

                search(
                    start = i,
                    remaining = remaining - choice,
                    current = current
                )

                current.pop()

        search(
            start = 0,
            remaining = target,
            current = []
        )

        # Time complexity - O(n^(t/m)) -> t is target, m is min val in given array, n is len(nums)
        # Space complexity - O(t/m) -> t is target, m is min val in given array

        return result