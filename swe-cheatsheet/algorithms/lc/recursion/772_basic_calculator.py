def calculate1(s: str) -> int:
    if not s: return 0
    l1_val, l1_op, l2_val, l2_op_mult = 0, 1, 1, True
    stack = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            n = int(c)
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
                n = n * 10 + int(s[i])

            l2_val = l2_val * n if l2_op_mult else l2_val / n  # always OK to apply nums at highest precedence
        elif c in ('+', '-'):
            if c == '-' and (i == 0 or s[i - 1] == '('):  # (-1) and -(1)
                l1_op = -1
            else:
                l1_val = l1_val + l1_op * l2_val  # resolve current multi
                l2_val, l2_op_mult = 1, True  # reset L2 (mult/div)
                l1_op = 1 if c == '+' else -1
        elif c in ('*', '/'):
            l2_op_mult = c == '*'
        elif c == '(':
            stack.append((l1_val, l1_op, l2_val, l2_op_mult))
            l1_val, l1_op, l2_val, l2_op_mult = 0, 1, 1, True
        elif c == ')':  # suspended * (current)
            n = l1_val + l1_op * l2_val  # calc current expression
            l1_val, l1_op, l2_val, l2_op_mult = stack.pop()  # bring back suspended expression
            l2_val = l2_val * n if l2_op_mult else l2_val / n  # fold current into suspended

        i += 1

    return l1_val + l1_op * l2_val


def operation(op, second, first):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":  # integer division
        return first // second

def precedence(current, previous):
    if previous in "()":
        return False
    if current in "*/" and previous in "+-":
        return False
    return True


def calculate(s):
    s = s.replace(' ', '')
    nums, ops = [], []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = int(c)
            while i < len(s) - 1 and s[i + 1].isdigit():
                num = num * 10 + int(s[i + 1])
                i += 1
            nums.append(num)
        elif c == "(":
            ops.append(c)
        elif c == ")":
            while ops[-1] != "(":
                nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
        elif c in "+-*/":
            while ops and precedence(current=c, previous=ops[-1]):
                nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            ops.append(c)
            if c == '-' and (not nums or s[i - 1] == '('):
                nums.append(0)

        i += 1

    while ops:
        nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

    return nums[-1] if nums else 0


def test():
    tests = [
        ('1 + 2 / 1 + (3 - (2*2))', 2),
        ('0', 0),
        ('(-1+1) + 1', 1),
        ('-(1 + 1) + 5 *2', 8),
        ("1 + 1", 2),
        (" 6-4 / 2 ", 4.0),
        ("2*(5+5*2)/3+(6/2+8)", 21.0),
        ("(2+6* 3+5- (3*14/7+2)*5)+3", -12.0),
    ]
    for s, expected in tests:
        actual = calculate(s)
        print(f'{s} = {actual}  ({expected})')


test()
