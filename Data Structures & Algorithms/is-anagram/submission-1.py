class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for char in s:
            dict_s[char] += 1
        for char in t:
            dict_t[char] += 1
        if dict_s == dict_t:
            return True
        return False