from typing import Optional


def first_recur_char(a: str) -> Optional[str]:
    seen = set()
    for c in a:
        if c in seen:
            return c
        seen.add(c)
    return None


# time O(n)
# space O(n) extra space
print(first_recur_char('qwertty'))
print(first_recur_char('qwerty'))
