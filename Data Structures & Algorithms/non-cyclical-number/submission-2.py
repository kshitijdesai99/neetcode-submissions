class Solution:
    def isHappy(self, n: int) -> bool:                   
        def square_sum(temp):
            output = 0
            while temp>=1:
                rem = temp%10
                output+=rem*rem
                temp = temp//10
                
            return output
        
        output = square_sum(n)
        mem = set()

        while output!=1:
            output = square_sum(output)
            if output in mem:
                return False
            mem.add(output)

        return True
        # Time complexity - O(log(n))
        # Space complexity - O(log(n))