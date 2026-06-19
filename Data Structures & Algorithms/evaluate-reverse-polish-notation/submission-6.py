class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens)==1:
            return(int(tokens[0]))
        for i in tokens:
            if i not in ("+","-","*","/"):
                stack.append(i)
            else:
                if(i=="+"):
                    a = int(stack[-2])+int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif(i=="-"):
                    a = int(stack[-2])-int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif(i=="*"):
                    print(stack)
                    a = int(stack[-2])*int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif(i=="/"):
                    a = int(stack[-2])/int(stack[-1])
                    a = int(a)
                    stack.pop()
                    stack.pop()
                    stack.append(a)

        return(stack[0])
