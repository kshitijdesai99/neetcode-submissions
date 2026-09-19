class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        output = 0
        for i in bin_n:
            if(i=='1'):
                output+=1
        return output
        # Time complexity - O(1) # 32 bit bounded
        # Space complexity - O(1)