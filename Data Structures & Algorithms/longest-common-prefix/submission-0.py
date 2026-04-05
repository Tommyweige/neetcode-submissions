class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = 9999
        for i in strs:
            size = min(size, len(i))

        output = ""
        char = ""
        for i in range(size):
            for j in range(len(strs)):
                char = strs[0][i]
                print(char)
                if strs[j][i] != char:
                    return output
            output += char
        return output

            


