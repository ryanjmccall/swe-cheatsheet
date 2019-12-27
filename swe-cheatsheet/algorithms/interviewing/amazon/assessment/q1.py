from collections import defaultdict


def popularNToys(numToys, topToys, toys, numQuotes, quotes):
    freq = defaultdict(int)
    quote_freq = defaultdict(int)
    removes = {'!', '.', '(', ')'}
    for quote in quotes:
        words = quote.lower().split()
        seen = set()
        for word in words:
            word = ''.join(filter(lambda c: c not in removes, word))
            if word not in seen:
                quote_freq[word] += 1
                seen.add(word)

    for toy in toys:
        freq[toy] += quote_freq[toy]

    res = sorted(freq.items(), key=lambda e: e[1], reverse=True)
    return [toy for toy, cnt in res[:topToys] if cnt]


def t():
    print(popularNToys(5, 2,
                 ['anacell', 'betacellular', 'cetracular', 'deltacellular', 'eurocell'], 3,
                 ['Best services provided by anacell', 'betacellular has great services',
                  'anacell provides much better services than all other']))

t()
