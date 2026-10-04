class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notations = ['+','-','*','/']
        stack = []
        for i in tokens:
            if i in notations:
                print("see " + i)
                b = stack.pop()
                a = stack.pop()
                print("a = {}, b = {}".format(a,b))
                if i == "+":
                    val = a + b
                    stack.append(val)
                elif i == '-':
                    val = a - b
                    stack.append(val)
                elif i == '*':
                    val = a * b
                    stack.append(val)
                elif i == "/":
                    val = int(a / b)
                    stack.append(val)
            else:
                stack.append(int(i))
                print("add " + i)
        return stack.pop()