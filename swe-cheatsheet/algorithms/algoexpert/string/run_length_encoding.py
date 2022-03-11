def runLengthEncoding(string: str) -> str:
    if not string: return ''
    if len(string) == 1: return string
    encodings = []
    seq_count = 1
    prev = string[0]
    for char in string[1:]:
        if prev != char:
            encodings.extend(get_encoding(prev, seq_count))
            seq_count = 0

        seq_count += 1
        prev = char

    encodings.extend(get_encoding(prev, seq_count))
    return ''.join(encodings)


def get_encoding(char: str, count: int) -> list:
    res = []
    while count:
        group_size = 9 if count > 9 else count
        res.append(f'{group_size}{char}')
        count -= group_size
    return res


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
