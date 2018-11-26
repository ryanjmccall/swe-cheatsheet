def removeDuplicateLetters0(s):
    """
    :type s: str
    :rtype: str
    """
    chars = dict()
    for i, c in enumerate(s):
        if c not in chars:
            chars[c] = i

    sortedEntries = sorted(chars.items(), key=lambda e: e[1])
    return "".join(e[0] for e in sortedEntries)





def removeDuplicateLetters3(s):
    charToIdx = {c: i for i, c in enumerate(s)}
    result = ''
    for i, c in enumerate(s):
        if c not in result:
            while c < result[-1] and i < charToIdx[result[-1]]:
                result = result[:-1]
            result += c
    return result


def removeDuplicateLetters2(s):
    result = ''
    while s:
        # for rightmost occurrence of each letter, take minimum
        i = min(map(s.rindex, set(s)))

        # min lexical order
        c = min(s[:i+1])
        result += c

        # toss front half, replacing used up char
        s = s[s.index(c):].replace(c, '')
    return result


from collections import Counter


def removeDuplicateLetters(s: str) -> str:
    if not s:
        return ""

    counter = Counter(s)
    pos = 0 # position of the lexically smallest char
    for i, c in enumerate(s):
        if c < s[pos]:
            pos = i

        counter[c] -= 1
        if not counter[c]:
            break

    subRes = removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))
    return s[pos] + subRes


print(removeDuplicateLetters("abcabc"))
print(removeDuplicateLetters("cbacba"))
print(removeDuplicateLetters("abcacb"))







