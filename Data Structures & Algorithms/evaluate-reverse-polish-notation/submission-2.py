class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = [tokens[0]]
        curr = int(tokens[0])
        ops = {'+', '-', '*', '/'}
        for i in range(1, len(tokens)):
            if not calc:
                calc.append(tokens[i])
            elif tokens[i] not in ops:
                calc.append(tokens[i])
            else:
                num1 = int(calc.pop())
                num2 = int(calc.pop())
                curr = int(eval(f'num2 {tokens[i]} num1'))
                calc.append(curr)
        return curr