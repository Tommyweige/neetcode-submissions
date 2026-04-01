from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed),reverse=True) # [(pos,speed),(4,2),(1,3)]
        output = 0
        curr_max_time = 0
        time = []
        for pos, s in cars:
            time.append((target-pos)/s)
        time = deque(time) # 將stack轉化爲 （Double-Ended Queue）。它是為了「兩端快速進出」設計的。
        while time:
            t = time.popleft()
            if t > curr_max_time:
                output += 1
                curr_max_time = t
        return output  