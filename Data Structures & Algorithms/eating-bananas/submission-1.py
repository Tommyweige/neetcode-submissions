class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper, lower, ans = max(piles), 1, 0
        

        while upper >= lower:
            mid = (upper + lower) // 2
            
            times = 0
            for i in piles:
                times += (i + mid - 1) // mid
            if times > h:
                lower = mid + 1
            else:
                ans = mid
                upper = mid - 1

            print(mid)
            print(times)
        return ans
            

            # times < h and mid < ans:
            # ans = mid
