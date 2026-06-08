class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dup = {}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if(dup.get(i)==None):
                dup[i]=1
            else:
                dup[i]+=1

        for i in t:
            print(i)
            if(dup.get(i)==None or dup.get(i)==0):
                return False
            else:
                dup[i]-=1
        return True