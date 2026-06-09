from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in strs:
            output = [0]*26
            for j in i:
                output[ord(j)-ord('a')]+=1
            groups[tuple(output)].append(i)  

        return(list(groups.values()))