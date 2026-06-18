class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map = {}
        t_map = {}

        for i in t:
            t_map[i] = t_map.get(i,0)+1
        
        required = len(t_map)
        len_s = len(s)

        formed = 0
        head = 0
        tail = 0
        max_len = float("inf")
        output = ""

        while(tail<len_s or formed==required):
            if(formed==required and head<tail):
                # start shrinking
                if(tail-head<max_len):
                    max_len = tail - head
                    output = s[head:tail]
                s_map[s[head]] -=1
                if(t_map.get(s[head])):
                    if(s_map.get(s[head])<t_map[s[head]]):
                        formed-=1
                head+=1
            else:
                # expand
                s_map[s[tail]] = s_map.get(s[tail],0) + 1
                if(s_map[s[tail]]==t_map.get(s[tail],None)):
                    formed+=1
                tail+=1

        return output
            
        