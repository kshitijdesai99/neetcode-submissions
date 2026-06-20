class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[i,j] for i, j in zip(position, speed)]
        stack = []
        for position,speed in sorted(pair)[::-1]:
            time = (target-position)/speed
            if(len(stack)>0 and time<=stack[-1]):
                pass
            else:
                stack.append(time)
        print(stack)
        return len(stack)