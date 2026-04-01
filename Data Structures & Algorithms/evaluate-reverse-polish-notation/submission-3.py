import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        operators = {"+": operator.add,
        "*": operator.mul,
        "-":operator.sub,
        "/":operator.truediv}

        for c in tokens:
            if c in operators:
                total = int(operators[c](int(stack[-2]),int(stack[-1])))
                stack.pop()
                stack.pop()
                stack.append(total)
            else:
                stack.append(c)
                total = int(c)

            print(stack)
        
        return total