class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def is_before(left, right):
            if(left[1]<right[0]):
                return True
            return False

        def merge_overalapping(left, right):
            min_0 = min(left[0],right[0])
            max_1 = max(left[1],right[1])
            return[min_0,max_1]

        def overlaps(left, right):
            return not is_before(left,right) and not is_before(right, left)

        result = []

        for inter in intervals:
            if is_before(inter, newInterval):
                result.append(inter)
            elif overlaps(inter, newInterval):
                newInterval = merge_overalapping(inter, newInterval)
            else:
                result.append(newInterval)
                newInterval = inter
                
        result.append(newInterval)
        # Time complexity - O(n)
        # Space complexity - O(1)
        return result