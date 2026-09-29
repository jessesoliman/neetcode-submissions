class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = [0] * 26
        for char in s:
            s_list[ord(char)-97] += 1
        for char in t:
            s_list[ord(char)-97] -= 1
        
        for i in range(len(s_list)):
            if s_list[i] != 0:
                return False
        return True
        
        