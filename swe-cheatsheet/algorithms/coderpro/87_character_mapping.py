


def char_mapping(a: str, b: str) -> bool:
    # leetcode isomorphic strings solution
    if len(a) != len(b):
        return False
    a2b, b2a = {}, {}
    for x, y in zip(a, b):
        if x not in a2b and y not in b2a:
            a2b[x] = y
            b2a[y] = x
        elif a2b.get(x) != y or b2a.get(y) != x:
            return False
    return True



    # techlead question
    # if len(a) != len(b):
    #     return False
    #
    # mapping = dict()
    # for x, y in zip(a, b):
    #     if x not in mapping:
    #         mapping[x] = y
    #     elif mapping[x] != y:
    #         return False
    #
    # return True


print(char_mapping('123456', 'def'))  # false
print(char_mapping('aac', 'def'))  # false
print(char_mapping('aac', 'eef'))  # True
print(char_mapping('abc', 'def'))  # true


