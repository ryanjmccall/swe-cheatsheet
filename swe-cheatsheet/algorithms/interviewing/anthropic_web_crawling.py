import os.path

import requests
from bs4 import BeautifulSoup
from typing import List
from collections import deque
from urllib.parse import urlparse
from urllib.parse import urljoin
from typing import Set


def get_links(url: str) -> List[str]:
    """Get all the links on a page."""
    page = requests.get(url)
    bs = BeautifulSoup(page.content, features='lxml')
    return [link.get('href') for link in bs.findAll('a')]


def clean_links(url: str) -> List[str]:
    result = set()
    netloc = urlparse(url).netloc
    for link in get_links(url):
        if '#' == link[0]:
            continue

        link_parse = urlparse(link)
        if link_parse.netloc == netloc:
            ext = os.path.splitext(link_parse.path)[1]
            if ext not in ('.html', '.htm'):
                continue

            link = link.strip()
            result.add(link)
        elif link_parse.netloc == '':
            link = urljoin(url, link).strip()
            result.add(link)

    return list(result)


def scrape_links(domain: str) -> Set[str]:
    q = deque([domain])
    visited = set()
    while q:
        cur = q.popleft()
        visited.add(cur)
        for link in clean_links(cur):
            if link not in visited:
                q.append(link)

        print(len(q))

    return visited


URL_ = 'http://www.cold-takes.com'
results_ = scrape_links(URL_)
for r in sorted(results_):
    print(r)

print('total results ', len(results_))
