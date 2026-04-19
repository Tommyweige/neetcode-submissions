class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            point = (right + left) // 2
            print(point)
            if nums[point] > target:
                right = point - 1
            elif nums[point] < target:
                left = point + 1
            else:
                return point
        return -1

        
        