class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dupes = set()
        length = 0
        for r, char in enumerate(s):
            if char not in dupes:
                dupes.add(char)
            elif s[l] == s[r]:
                l += 1
            else:
                while s[l] != s[r]:
                    dupes.remove(s[l])
                    l += 1
                dupes.remove(s[l])
                l += 1
                dupes.add(char)
            length = max(length, r - l + 1)
        if len(s) == 0:
            return 0
        return length