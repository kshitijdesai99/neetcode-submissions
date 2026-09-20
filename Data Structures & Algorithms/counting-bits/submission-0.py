class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            temp = 0
            for j in bin(i):
                if(j=='1'):
                    temp+=1
            output.append(temp)
        # Time complexity - O(n)
        # Space complexity - O(1)
        return output