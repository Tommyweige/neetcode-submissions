import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = int(tokens[0])

        # 使用operator來處理字串轉運算元

        operators = {"+": operator.add,
        "*": operator.mul,
        "-":operator.sub,
        "/":operator.truediv}

        # 掃描整個串列
        for c in tokens:
            # 當輸入是operators其中一個時
            if c in operators:
                # 將 stack 中的最後兩個元素做運算，存入total
                total = int(operators[c](int(stack[-2]),int(stack[-1])))
                # 將最後兩個元素pop出來，然後push結果（total），以便下一次運算
                stack.pop()
                stack.pop()
                stack.append(total)
            else:
                # 如果是數字就直接push
                stack.append(c)

        return total