class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res =[0] * len(temperatures)
        stack = [] # [temp, index]
        for idx,tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                currTmp, currIdx = stack.pop()
                res[currIdx] = idx - currIdx
            stack.append([tmp,idx])
        return res
