class Solution:
    def isHappy(self, n: int) -> bool:        
        def num_splitter(temp):
            digits = []
            while temp>=1:
                rem = temp%10
                digits.append(rem)
                temp = temp//10
            return digits

        def square_sum(digits):
            output = 0
            for i in digits:
                output+=i*i
            return output
        
        digits = num_splitter(n)
        output = square_sum(digits)
        mem = set()

        while output!=1:
            digits = num_splitter(output)
            output = square_sum(digits)
            if output in mem:
                return False
            mem.add(output)

        return True
        # Time complexity - O(log(n))
        # Space complexity - O(log(n))