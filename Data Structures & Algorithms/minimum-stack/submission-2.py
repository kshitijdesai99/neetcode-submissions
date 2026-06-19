class MinStack:

    def __init__(self):
        self.stack = []
        self.global_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, self.global_min))
        if(val<self.global_min):
            self.global_min = val
        
    def pop(self) -> None:
        self.global_min = self.stack[-1][1]
        self.stack.pop()

    def top(self) -> int:
        return(self.stack[-1][0])

    def getMin(self) -> int:
        return(self.global_min)
