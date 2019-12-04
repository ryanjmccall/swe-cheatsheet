_CLOSE_TO_OPEN = {']': '[', ')': '(', '}': '{'}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in _CLOSE_TO_OPEN:
                if stack and stack[-1] == _CLOSE_TO_OPEN[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


print(Solution().isValid("()[]{}"))
