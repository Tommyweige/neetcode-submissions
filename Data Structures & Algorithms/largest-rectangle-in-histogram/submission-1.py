class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0
        
        for i, height in enumerate(heights):
            start_idx = i
            
            # 如果在結束前，目前元素比 stack 頂端元素小或相等，則 pop 並結算面積
            while stack and stack[-1][1] >= height:
                # 寬度不需要加絕對值，直接用目前的 i 減去 stack 內記錄的 index
                if stack[-1][1] * (i - stack[-1][0]) > output:
                    output = stack[-1][1] * (i - stack[-1][0])
                
                start_idx, _ = stack.pop()

            stack.append([start_idx, height])
            
        # 當執行到最後時，開始做後續處理
        # 此時的「最右邊界」是陣列的總長度 len(heights)
        n = len(heights)
        while stack:
            if stack[-1][1] * (n - stack[-1][0]) > output:
                output = stack[-1][1] * (n - stack[-1][0])
            stack.pop()

        return output