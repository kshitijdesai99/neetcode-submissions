class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_idx = []
        output = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while(len(stack_idx)>0 and temperatures[i]>temperatures[stack_idx[-1]]):
                old_idx = stack_idx.pop()
                output[old_idx] = i - old_idx

            stack_idx.append(i)
        return(output)