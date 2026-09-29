class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = [char.lower() for char in s if char.isalnum()]
        print(str_list)
        for i in range(len(str_list)//2):
            if str_list[i] == str_list[-i-1]:
                continue
            return False
        return True