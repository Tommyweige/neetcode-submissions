class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        # 保持你的一行初始化風格
        l, r, lmax, rmax, total = 0, len(height) - 1, height[0], height[-1], 0

        while l < r:
            if lmax <= rmax:
                # 既然 lmax 比較矮，我們就處理左邊往右的下一格 (l+1)
                l += 1
                total += max(lmax - height[l], 0)
                lmax = max(lmax, height[l])
            else:
                # 同理，處理右邊往左的下一格 (r-1)
                r -= 1
                total += max(rmax - height[r], 0)
                rmax = max(rmax, height[r])
                
        return total