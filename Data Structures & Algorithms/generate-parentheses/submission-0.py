class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def recurParenthesis(n, l , r, para):
            if n == 0:
                res.add(para)
                return
            elif n == l == r: # if all equal, add left, start condition
                recurParenthesis(n, l - 1, r, para + '(')
            elif l < r and r == n: # else if l < r, can add a left or right
                if l > 0: # we can add left and right
                    recurParenthesis(n, l - 1, r, para + '(')
                    recurParenthesis(n - 1, l , r - 1, para + ')')
                else: # can only add right
                    recurParenthesis(n - 1, l, r - 1, para + ')')
      
        recurParenthesis(n, n, n, "")

        return list(res)