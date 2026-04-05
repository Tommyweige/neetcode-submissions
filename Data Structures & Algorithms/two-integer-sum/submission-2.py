class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in hashmap:
                return [hashmap[ans], i]
            hashmap[num] = i