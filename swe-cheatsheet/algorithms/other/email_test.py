raw = 'john123@sprng.edu.in'


def is_valid(email_: str) -> bool:
    # 1
    splits = email_.split('@')
    if len(splits) != 2:
        return False

    if not all(splits):
        return False

    part_1, part_2 = splits

    # 2
    if not part_1.isalnum():
        return False

    if not part_1[0].isalpha():
        return False

    # 3
    p2_splits = part_2.split('.')
    if len(p2_splits) not in (2, 3):
        return False

    if not all(p2_splits):
        return False

    # 4
    segments = p2_splits[:-1]
    for seg in segments:
        if not seg.isalnum():
            return False

    # 5
    last_segment = p2_splits[-1]
    if len(last_segment) not in (2, 3):
        return False
    if not last_segment.isalpha():
        return False

    return True


print('Valid' if is_valid(raw) else 'Invalid')
