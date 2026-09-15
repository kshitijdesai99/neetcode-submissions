class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        newInterval = intervals[0]
        def can_merge(left,right):
            if(left[0]<=right[1] and left[1]>=right[0]):
                return True
            return False
        
        def merge_helper(left,right):
            left_min = min(left[0], right[0])
            right_max = max(left[1], right[1])
            return([left_min, right_max])

        output = []
        i = 1
        while(i<len(intervals)):
            while(i<len(intervals) and can_merge(newInterval,intervals[i])):
                newInterval = merge_helper(newInterval,intervals[i])
                i+=1
            else:
                if(i<len(intervals)):
                    output.append(newInterval)
                    newInterval = intervals[i]
            i+=1
            
        output.append(newInterval)
        # Space complexity - O(nlogn)
        # Time complexity - O(1)

        return output