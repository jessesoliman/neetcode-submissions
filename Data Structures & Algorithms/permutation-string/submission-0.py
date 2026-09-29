class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            s2_dict = Counter(s2[i:i+len(s1)])
            if s1_dict == s2_dict:
                return True
        return False


#AAAAAAAA
# AAA