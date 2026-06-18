class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if(s1_len > s2_len):
            return False

        s1_list = [0]*26
        s2_list = s1_list.copy()

        for i in range(s1_len):
            s1_list[ord(s1[i])-ord('a')] += 1
            s2_list[ord(s2[i])-ord('a')] += 1

        if(s1_list==s2_list):
            return True

        for i in range(s1_len, s2_len, 1):
            s2_list[ord(s2[i])-ord('a')]+=1
            s2_list[ord(s2[i-s1_len])-ord('a')]-=1

            if(s1_list==s2_list):
                return True

        return False

        