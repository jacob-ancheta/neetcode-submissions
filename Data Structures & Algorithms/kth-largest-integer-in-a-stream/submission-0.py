class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
    [1, 2, 3, 3, 3] [3]
    [1, 2, 3, 3, 3, 5] [3]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        largest = float('-inf')
        for i, num in enumerate(reversed(self.nums)):
            largest = num
            if (i + 1) == self.k:
                return num
        return 1
            








    