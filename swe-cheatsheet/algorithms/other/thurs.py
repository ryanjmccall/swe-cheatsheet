# 1) Create implementation of github account search, which accepts an account
#  name, to be searched at https://api.github.com/users/<username>
#
# search(term=’bob’)
#
# True
#
# search(term=’dfshdlfkjsdlkfjsdlkfjsdlkfjs’)
#
# False

import requests
from requests import RequestException


VALID_RESPONSE = (200,)

MISSING_PERSON = (404,)


def search(term: str) -> bool:
    term = term.strip().lower()
    baseUrl = "https://api.github.com/users"
    fullUrl = "/".join((baseUrl, term))

    try:
        r = requests.get(fullUrl)
    except RequestException:
        raise RuntimeError("Can't be determined")

    if r.status_code in VALID_RESPONSE:
        return True
    elif r.status_code in MISSING_PERSON:
        return False

    raise RuntimeError("Can't be determined")


# print(search("ryanjmccall"))
# print(search("alsfkjasldkj"))

# term is None
# term contains /, non-printing, newline
# term cases
# term super long


# 2) Extend the function to search at arbitrary depths
#
# search(name=’bob’, depth=0)
#
# [‘bob’]
#
# search(name=’bob’, depth=1)
#
# [‘bob’, ‘boba’, ‘bobb’, … ‘bobz’]
#
# search(name=’bob’, depth=2)
#
# [‘bob’, ‘boba’, ‘bobaa’, ‘bobab’, … ‘bobzz’]
#
# O(b^depth)

from typing import Generator
from collections import deque


ALPHA = "abcd"


def search(name: str, depth: int) -> Generator[str, None, None]:
    q = deque([(name, depth)])
    while q:
        prefix, d = q.popleft()
        if d:
            q.extend((prefix + letter, d - 1) for letter in ALPHA)

        yield prefix


print(list(search("ryan", depth=0)))
print(list(search("ryan", depth=1)))
print(list(search("ryan", depth=2)))

