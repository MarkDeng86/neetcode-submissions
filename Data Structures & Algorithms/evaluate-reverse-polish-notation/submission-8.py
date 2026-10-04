class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notations = ['+','-','*','/']
        stack = []
        for i in tokens:
            if i == "+":
                a, b = stack.pop(), stack.pop()
                val = a + b
                stack.append(val)
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                val = b - a
                stack.append(val)
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                val = a * b
                stack.append(val)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                val = int(b / a)
                stack.append(val)
            else:
                stack.append(int(i))
                print("add " + i)
        return stack.pop()