class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        longest = 1

        for r, char in enumerate(s):
            if char not in chars:
                chars.add(char)
            else:
                window = False
                while not window:
                    if s[l] == s[r]:
                        l += 1
                        window = True
                    elif s[l] in chars:
                        chars.remove(s[l])
                        l += 1
                    
            longest = max(longest, (r - l) + 1)
        if not s:
            return 0
        return longest