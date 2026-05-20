class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        end = len(nums) - 1

        while front <= end:
            mid = (front + end) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                front = mid + 1
            else:
                end = mid - 1
        return -1