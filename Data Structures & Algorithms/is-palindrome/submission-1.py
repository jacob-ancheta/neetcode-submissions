class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list_s = list(filter(str.isalnum,s))

        j = len(list_s) - 1
        for i in range(len(list_s)):
            if j == i or j <= i:
                return True
            if list_s[i] != list_s[j]:
                return False
            j -= 1
        return True
            

