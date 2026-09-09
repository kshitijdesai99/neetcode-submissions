class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def search(curr,start):
            nonlocal result

            if curr not in result:
                result.append(curr.copy())

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                search(
                    curr = curr,
                    start = i+1
                )
                curr.pop()

        search(
            curr = [],
            start = 0
        )

        return result