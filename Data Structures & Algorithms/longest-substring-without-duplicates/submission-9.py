class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        parent = 0
        max_len = 0
        char_map = {}

        for child in range(len(s)):
            char_map[s[child]] = char_map.get(s[child],0)+1
            while(char_map[s[child]]>1):
                char_map[s[parent]]-=1
                parent+=1
                
            max_len = max(max_len, child-parent+1)

        return max_len