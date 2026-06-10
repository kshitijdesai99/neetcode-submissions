class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if nums_dict.get(i):
                nums_dict[i]+=1
            else:
                nums_dict[i]=1
        

        temp_list = [[] for i in range(len(nums)+1)]

        for key, value in nums_dict.items():
            temp_list[value].append(key)
        
        output = []
        for i in range(len(temp_list)-1, 0, -1):
            output.extend(temp_list[i])
            if len(output)==k:
                return output