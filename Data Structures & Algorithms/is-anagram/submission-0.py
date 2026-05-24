class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dict = {}
        s_dict = {}
        for char in s:    
            if char not in s_dict:
                s_dict[char] = 1
            if char in s_dict:
                s_dict[char] += 1
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            if char in s_dict:
                t_dict[char] += 1
        if t_dict == s_dict:
            return True
        else:
            return False

    