class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums.sort()
        print(nums)

        for i ,a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else: 
                    output.append([a,nums[left],nums[right]])
                    left += 1
                    # 跳過接下來會重複的數字
                    while left <= right and nums[left] == nums[left - 1]:
                        left += 1
        return output



        