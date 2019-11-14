_ALL_BRACKETS = {'[', ']', '{', '}', '(', ')'}
_LEFT_BRACKETS = {'[', '{', '('}
_RIGHT_MATCH = {']': '[', ')': '(', '}': '{'}

input_ = ')'
brackets = ''.join((s for s in input_ if s in _ALL_BRACKETS))


def is_balanced() -> bool:
    stack = []
    for b in brackets:
        if b in _LEFT_BRACKETS:
            stack.append(b)
        else:

            if not stack:
                return False

            actual_value = stack[-1]
            expected_value = _RIGHT_MATCH[b]
            if actual_value == expected_value:
                stack.pop()
            else:
                return False

    return len(stack) == 0


_is_bal = 'Y' if is_balanced() else 'N'
print('{} {}'.format(_is_bal, brackets))



