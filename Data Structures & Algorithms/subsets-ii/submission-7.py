class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def search(curr,start):
            nonlocal result
            temp = curr.copy()
            temp.sort()
            if temp not in result:
                result.append(temp.copy())

            for i in range(start,len(nums)):
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