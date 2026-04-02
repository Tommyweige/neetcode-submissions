import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        head, tail = 0, len(s)-1
        while head != tail and head <= tail:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
            print(head)
        return True
