class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def search(start, remainder, curr):
            if remainder == 0:
                nonlocal result
                result.append(curr.copy())
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i]>remainder:
                    break

                curr.append(candidates[i])
                search(
                    start = i+1,
                    remainder = remainder - candidates[i],
                    curr = curr
                )
                curr.pop()

        search(
            start = 0,
            remainder = target,
            curr = []
        )
        # Time complexity - O(n*(2*m))
        # Space complexity - O(n)
        return result