import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 使用 regex 去除除了(A-Z, a-z, 0-9)的其他符號，並且都轉成小寫
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # 使用雙指標來掃描正反是否一致
        head, tail = 0, len(s)-1
        while head <= tail:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
