class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]


a = Solution()

assert a.evalRPN(["2","1","+","3","*"]) == 9
assert a.evalRPN(["4","13","5","/","+"]) == 6
assert a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
