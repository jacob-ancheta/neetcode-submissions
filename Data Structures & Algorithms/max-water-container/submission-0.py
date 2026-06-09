class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0   
        r = n - 1
        maxHeight = float('-inf')
        while l < r:
            maxHeight = max((r - l) * min(heights[r],heights[l]), maxHeight)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxHeight
