class Solution:

    def encode(self, strs: List[str]) -> str:
        return("".join([f"{len(i)}#{i}" for i in strs]))
    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while(i<len(s)):
            j = i
            while(s[j]!="#"):
                j+=1
            count=int(s[i:j])
            output.append(s[j+1:j+count+1])
            i=j+count+1

        return(output)
