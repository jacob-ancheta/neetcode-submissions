class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []
       
        def backtrack(i, total):
            if total == target and sol[:] not in ans:
                ans.append(sol[:])
            if total > target or i == len(nums):
                return
            
            sol.append(nums[i])
            backtrack(i, total + nums[i])
            sol.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return ans
                

            