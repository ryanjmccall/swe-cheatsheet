from typing import List


digit_to_letter = {
    0: [],
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


def words_for_number(num: List[int], words: List[str]) -> List[str]:
    trie = dict()
    for w in words:
        cur = trie
        for c in w:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

    res = []
    def dfs(trie_ptr: dict, prefix: str, digits: list):
        if not digits:
            if prefix in words:
                res.append(prefix)
            return

        for letter in digit_to_letter[digits[0]]:
            if letter in trie_ptr:
                dfs(trie_ptr=trie_ptr[letter], prefix=prefix + letter, digits=digits[1:])

    dfs(trie_ptr=trie, prefix='', digits=num)
    return res


print(words_for_number(num=[3, 6, 4], words=['dog', 'cat', 'fish', 'fog']))
