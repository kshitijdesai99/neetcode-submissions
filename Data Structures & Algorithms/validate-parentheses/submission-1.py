class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif par_dict.get(stack[-1],None)!=i:
                stack.append(i)
            else:
                stack.pop()
        
        if(len(stack)==0):
            return True
        
        return False