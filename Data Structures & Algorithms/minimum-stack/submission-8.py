class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.global_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(val<=self.global_min):
            self.min_stack.append(val)
            self.global_min = val
        if(len(self.min_stack)==0):
            self.min_stack.append(val)
        # print("push",self.stack,self.min_stack)
        
    def pop(self) -> None:
        if(self.stack[-1]==self.min_stack[-1]):
            self.global_min = self.min_stack[-1]
            self.min_stack.pop()
        self.stack.pop()
        # print("pop",self.stack,self.min_stack)

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        return(self.min_stack[-1])
