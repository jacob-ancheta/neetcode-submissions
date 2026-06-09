class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while r - l > 1:
            mid = (r + l) // 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r = mid
            else:
                l = mid
        if target >= matrix[r][0]:
            iterate = r
        else:
            iterate = l
        for i in matrix[iterate]:
            if target == i:
                return True
        return False

                