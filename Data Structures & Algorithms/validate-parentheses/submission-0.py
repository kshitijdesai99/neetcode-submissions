class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        queue = []
        for i in s:
            if len(queue)==0:
                queue.append(i)
            elif par_dict.get(queue[-1],None)!=i:
                queue.append(i)
            else:
                queue.pop()
        
        if(len(queue)==0):
            return True
        
        return False