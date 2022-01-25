from collections import Counter
from typing import Optional


def check_palindrome(a: str) -> Optional[str]:
    c = Counter(a)
    pre = ''
    mid = ''
    for i, count in c.items():
        if count % 2 == 1:
            if mid != '':
                return None

            mid = i

        pre += i * (count // 2)

    return pre + mid + pre[::-1]


assert check_palindrome('a') == 'a'
assert check_palindrome('abc') == None
assert check_palindrome('aba') == 'aba'
assert check_palindrome('baa') == 'aba'
assert check_palindrome('ababa') == 'ababa'
assert check_palindrome('ababad') == None
assert check_palindrome('abcabc') == 'abccba'
