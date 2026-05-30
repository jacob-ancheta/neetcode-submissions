class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while r - l > 1:
            mid = l +((r - l) // 2)
            if target <= matrix[mid][0]:
                r = mid
            else:
                l = mid
        row = l if target < matrix[r][0] else r
        for i in matrix[row]:
            if target == i:
                return True
        return False
