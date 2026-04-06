class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] == res:
                count+=1
            elif res != nums[i] and count == 0:
                res = nums[i]
                count = 1
            else:
                count -= 1
            print(f"i: {i} res: {res} count: {count}")
        return res
        