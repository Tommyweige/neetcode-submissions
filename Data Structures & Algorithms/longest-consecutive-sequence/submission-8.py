class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = nums
        longest = 0

        for i in num:
            if i - 1 not in num:
                length = 0
                while i + length in num:
                    length += 1
                longest = max(length,longest)
        return longest