class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parentheses = 0
        curly = 0
        bracket = 0
        for i in range(len(s)):
            if s[i] == '(':
                parentheses += 1
            elif s[i] == ')':
                if parentheses == 0:
                    return False
                if s[i-1] == '[' or s[i-1] == '{':
                    return False
                parentheses -= 1
            elif s[i] == '{':
                curly += 1
            elif s[i] == '}':
                if curly == 0:
                    return False
                if s[i-1] == '[' or s[i-1] == '(':
                    return False
                curly -= 1
            elif s[i] == '[':
                bracket += 1
            elif s[i] == ']':
                if bracket == 0:
                    return False
                if s[i-1] == '(' or s[i-1] == '{':
                    return False
                bracket -= 1
        if curly != 0 or parentheses != 0 or bracket != 0:
            return False
        return True
