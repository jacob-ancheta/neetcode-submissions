class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)
        used = [False] * n
        
        def backtrack():
            if len(sol) == len(nums):
                ans.append(sol[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                sol.append(nums[i])

                backtrack()

                sol.pop()
                used[i] = False

        backtrack()
        return ans