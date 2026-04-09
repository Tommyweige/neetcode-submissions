class Solution:
    def trap(self, height: List[int]) -> int:

        l ,r ,lmax ,rmax ,total = 0 ,len(height) - 1 ,height[0] ,height[-1] ,0

        while l < r:
            if lmax <= rmax:
                total += max(min(lmax, rmax) - height[l], 0)
                l += 1
                lmax = max(lmax, height[l])
            else:
                total += max(min(lmax, rmax) - height[r], 0)
                r -= 1
                rmax = max(rmax, height[r])
        return total

