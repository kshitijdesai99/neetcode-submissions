class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1,n+1):
            quotient = i//2
            remainder = i%2
            sumz = output[quotient]+remainder
            output.append(sumz)
        # Time complexity - O(n)
        # Space complexity - O(n)
        return output