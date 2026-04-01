class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for s in strs: # 歷遍strs裏面的每一個字串
            count = [0] * 26
            for w in s: # 歷遍strs裏面的每一個字串的每一個字母
                count[ord(w) - ord("a")] =  count[ord(w) - ord("a")] + 1 # 計算每一個字母出現的頻率，加入count中
            output[tuple(count)].append(s) # 在 output 這個字典中， key設爲 count ，value 設爲原始的單字s
        return list(output.values()) # 由於回傳的要是list，並且只需要他的values
