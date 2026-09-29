class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict_s[s[i]] += 1
            dict_t[t[i]] += 1
        return dict_t == dict_s