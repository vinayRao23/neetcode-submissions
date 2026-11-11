import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "*":
                stack.append(stack.pop() * stack.pop())
            elif val == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif val == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(val))
        
        return stack[0]