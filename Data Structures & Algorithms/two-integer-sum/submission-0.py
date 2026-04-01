class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            component = target - nums[i]
            if component in arr:
                return [arr[component], i]
            arr[nums[i]] = i
        return []