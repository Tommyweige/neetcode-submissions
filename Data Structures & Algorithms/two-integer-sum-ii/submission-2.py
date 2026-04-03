class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            if numbers[head] + numbers[tail] == target:
                return [head+1, tail+1]
            
            # tail leftshift cause smaller sum
            if numbers[head] + numbers[tail] > target:
                tail -= 1
                continue
            # head right shift cause bigger sum
            else:
                head += 1
