class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vals = set()

        for i in nums:
            if i in vals:
                vals.remove(i)
            else:
                vals.add(i)
        if vals:
            return vals.pop()
        else:
            return 0