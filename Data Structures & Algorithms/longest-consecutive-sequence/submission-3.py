class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 建立一個長度爲最大跟最小數字加總的陣列
        # lower_bound爲最小的數字
        # upper_bound爲最大的數字
        lower_bound = min(0,min(nums, default = 0))
        upper_bound = max(nums,default=0)

        ans = [0] * (upper_bound - lower_bound + 1)

        # offset爲最小數當作0開始
        # 由於陣列裏面會遇到[-1]，這表示從陣列的最後一個元素開始，避免這樣，需要使用offset，從ans[0]開始計算

        for i in nums:
            ans[i - lower_bound] = 1        

        temp = 0
        count = 0
        for i in range(len(ans)):
            # 如果ans[i]沒有元素，則中斷計數
            if ans[i] == 0:
                temp = 0
            else:
                temp += 1
            # 當temp比count大的時候就更新count
            if temp > count:
                count = temp
            
        return count
                
            