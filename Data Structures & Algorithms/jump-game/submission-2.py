class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        target = n
        while n>=0:
            if n + nums[n] >= target:
                print(target,n)
                target = n
            n-=1
        if target==0:
            return True
        return False