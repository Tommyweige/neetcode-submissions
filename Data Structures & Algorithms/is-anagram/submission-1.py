class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        arr1 = {}
        arr2 = {}
        
        for i in range(len(s)):
            arr1[s[i]] = arr1.get(s[i], 0) + 1
            arr2[t[i]] = arr2.get(t[i], 0) + 1
        if arr1 == arr2:
            return True
        return False
        