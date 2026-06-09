class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        already_added = set()
        for i in range(0, len(strs)):
            if(i in already_added):
                continue
            temp = [strs[i]]
            temp_i = "".join(sorted(strs[i]))
            for j in range(i+1, len(strs)):
                if(j in already_added):
                    continue
                temp_j = "".join(sorted(strs[j]))
                if(temp_i == temp_j):
                    temp.append(strs[j])
                    already_added.add(j)
            already_added.add(i)
            output.append(temp)
        return(output)