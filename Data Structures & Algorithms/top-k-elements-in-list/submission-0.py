class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if nums_dict.get(i):
                nums_dict[i]+=1
            else:
                nums_dict[i]=1
        nums_list = []
        for key, value in nums_dict.items():
            nums_list.append((key,value))
        nums_list.sort(key = lambda x : x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(nums_list[i][0])
        return output