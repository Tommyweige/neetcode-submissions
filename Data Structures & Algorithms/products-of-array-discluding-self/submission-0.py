class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right , left, ans, total  = [], [], [], 1 # 建立掃描的串列跟加總的暫時空間
        left.append(1)
        right.append(1)

        for i in range(0, len(nums)-1):
            """
            計算由前往後的每一個數字相乘的加總

            ex Input: nums = [1,2,4,6]
            left = [1, 1, 2, 8]

            """
            total *= nums[i] 
            left.append(total)
        total = 1

        for i in range(len(nums)-1 ,0,-1):
            """
            計算由後往前的每一個數字相乘的加總

            ex Input: nums = [1,2,4,6]
            right = [1, 6, 24, 48]
            
            """
            total *= nums[i] 
            right.append(total)
        right.reverse()
        for i in range(len(nums)):
            ans.append(left[i] * right[i])
        return ans


        

