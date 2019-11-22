

class Solution(object):
    SIGNS = {'+': 1, '-': -1}

    def evalute_expression(self, expression: str) -> int:
        expression = expression.replace(' ', '')
        result, _ = self._eval(expression, index=0)
        return result

    def _eval(self, expression: str, index: int) -> (int, int):
        result = 0
        sign = 1
        while index < len(expression):
            c = expression[index]
            if c in self.SIGNS:
                sign = self.SIGNS[c]
            elif c.isnumeric():
                result += sign * int(c)
            elif c == '(':
                val, index = self._eval(expression, index + 1)
                result += sign * val
            elif c == ')':
                break

            index += 1

        return result, index


print(Solution().evalute_expression(expression='-(3 + (2 - 1))'))  # -4
print(Solution().evalute_expression(expression='((5 - 4) - (-3 + 4))'))  # 0
