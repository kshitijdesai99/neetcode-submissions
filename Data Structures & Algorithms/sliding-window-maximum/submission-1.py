from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        idx_deque = deque([])

        for i in range(len(nums)):
            window_start = i-k+1
            
            # remove old indices from front
            if(len(idx_deque)!=0 and idx_deque[0]<window_start):
                idx_deque.popleft()

            # remove smaller values from back
            while(len(idx_deque)!=0 and nums[i]>nums[idx_deque[-1]]):
                idx_deque.pop()

            # add current indx
            idx_deque.append(i)

            # add value to output
            if i>=k-1:
                output.append(nums[idx_deque[0]])

        return output
