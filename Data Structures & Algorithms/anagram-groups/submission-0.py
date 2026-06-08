class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            chrs = [0]*26
            for c in str:
                chrs[ord(c)-ord('a')]+=1
            res[tuple(chrs)].append(str)
        return list(res.values())
        