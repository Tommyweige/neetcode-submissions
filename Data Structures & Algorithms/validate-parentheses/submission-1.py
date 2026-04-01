class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {"]":"[", "}":"{", ")":"("}
        for c in s: # 從串列中讀取字元
            if c in table: # 如果讀取的字元是close符號，如 ] } )
                if stack and stack[-1] == table[c]: # 如果stack的最後一個元素是對應C的open符號，如 [ { (
                    stack.pop()
                else: # 不是就回傳錯誤
                    return False
            else: # 如果是open符號就加入stack中
                stack.append(c)
        return True if not stack else False # 如果stack裏面沒有符號就回傳True

            