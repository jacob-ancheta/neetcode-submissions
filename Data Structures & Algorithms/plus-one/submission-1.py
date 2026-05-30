class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = len(digits) - 1
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        while curr > -1:
            if digits[curr] == 9:
                if curr == 0:
                    digits[curr] = 1
                    digits.append(0)
                    return digits
                elif digits[curr] == 9:
                    digits[curr] = 0
                    if digits[curr - 1] == 9:
                        curr -= 1
                    else:
                        digits[curr - 1] += 1
                        return digits