
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # 建立一個list 來記錄每一個數字出現的頻率
        freq = [[]for i in range(len(nums)+1)] # 建立一個長度爲nums的二維陣列當作bucket，之所以是二維是有可能同一個頻率會出現兩個數字
        ans = []

        for i in nums:
            '''
            將數字出現的頻率填入
            ex.1 
            {1:1,
            2:2,
            3:3}
            '''
            count[i] += 1

        for num, cnt in count.items():
            """
            從count的格式轉化爲稀疏矩陣

            如
            [[][1][2][3]]
            """
            freq[cnt].append(num)

        for i in range(len(freq) -1, 0, -1): # 從freq後面開始，掃描到0，步長爲-1
            for num in freq[i]: 
                ans.append(num)
                if len(ans) == k:
                    return ans

            





            