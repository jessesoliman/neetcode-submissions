class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurParenthesis(n, l , r, para):
            if n == 0:
                res.append(para)
                return
            
            #if n == l == r: # if all equal, add left, start condition
                #recurParenthesis(n, l - 1, r, para + '(')
            #elif l < r and r == n: # else if l < r, can add a left or right
            if l > 0: # we can add left and right
                recurParenthesis(n, l - 1, r, para + '(')
            if r > l:
                recurParenthesis(n - 1, l, r - 1, para + ')')
      
        recurParenthesis(n, n, n, "")

        return res