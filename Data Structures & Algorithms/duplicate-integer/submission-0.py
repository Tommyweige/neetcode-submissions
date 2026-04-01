class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = {}
        for i in range(len(nums)):
            if nums[i] in arr:
                return True
            arr[nums[i]] = i
        return False
