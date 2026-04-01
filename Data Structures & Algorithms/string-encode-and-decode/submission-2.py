class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i) ) + "#" + i # 5#hello5#world
        return ans


    def decode(self, s: str) -> List[str]:
        # print(int(s[0]))
        ans , i = [], 0 # 計算在字串中的位置,並且建立一個最後輸出地List
        while i < len(s): # 掃描整段的字串 
            j = i # i爲起始位置，j爲#前的位置
            while s[j] != "#": # 當遇到#之前，都會是這個字串的長度
                j += 1
            length = int(s[i : j]) # 長度爲#以前的數字
            ans.append(s[j+1 : j + length + 1]) # 因爲j在#這個位置，所以要append # + 1的位置就是字串開始的位置
            i = length + j + 1 # 將i的位置設爲 下一段數字長度的開始的位置
        return ans
 