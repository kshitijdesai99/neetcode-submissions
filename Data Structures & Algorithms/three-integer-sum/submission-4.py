class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputs = set()
        for i in range(2,len(nums)):
            j = len(nums)-1
            k = 0
            target = nums[i]
            while(k<j):
                if(nums[k]>target or k==i):
                    break
                elif(j==i):
                    j-=1
                elif(nums[k]+nums[j]==-target):
                    outputs.add(tuple(sorted(((nums[k],nums[j],target)))))
                    j-=1
                elif(nums[k]+nums[j]>-target):
                    j-=1
                else:
                    k+=1

        return([list(i) for i in outputs])