class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 找出所有字串中最短的長度
        size = min(len(s) for s in strs)

        output = ""
        for i in range(size):
            # 拿第一個字串的第 i 個字當作基準
            char = strs[0][i]
            
            # 檢查其他所有字串的第 i 個字
            for j in range(1, len(strs)): # 從第二個字串開始比即可
                if strs[j][i] != char:
                    return output
            
            # 如果大家都一樣，才加進 output
            output += char
            
        return output