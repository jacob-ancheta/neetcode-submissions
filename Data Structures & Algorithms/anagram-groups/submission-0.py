class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort not in key:
                key[sort] = [string]
            else:
                key[sort].append(string) 
        return list(key.values())