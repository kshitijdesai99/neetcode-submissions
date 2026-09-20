class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        helper_dict = {}
        for i in range(n+1):
            quotient = i//2
            remainder = i%2
            if not helper_dict.get(quotient):
                sumz = quotient+remainder
                output.append(sumz)    
            else:
                sumz = helper_dict[quotient]+remainder
                output.append(sumz)
            helper_dict[i] = sumz
        # Time complexity - O(n)
        # Space complexity - O(n)
        return output