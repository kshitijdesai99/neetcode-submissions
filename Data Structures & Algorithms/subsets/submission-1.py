class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Step 1 - init output
        output = [[]]

        # Step 2 - start going through each pass while extracting elements from output and adding it to that
        for i in nums:
            temp = []
            for j in output:
                temp.append(j+[i])
            output.extend(temp)
        # time compelexity - O(n*2^n)
        # space complexity - O(1)

        return output