class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
         
        for i,num in enumerate(nums):
            mult = 1
            temp = nums[:]
            temp.pop(i)
            for x in temp:
                mult *= x
            ans[i] = mult
        return ans