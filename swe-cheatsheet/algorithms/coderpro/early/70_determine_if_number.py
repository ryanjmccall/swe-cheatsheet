from enum import Enum


class DigitState(Enum):
    BEGIN = 0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT = 3
    DIGIT2 = 4
    E = 5
    NEGATIVE2 = 6
    DIGIT3 = 7


NEXT_STATES = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3],
}


STATE_VALIDATOR = {
    DigitState.BEGIN: lambda x: True,
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.NEGATIVE1: lambda x: x == '-',
    DigitState.DOT: lambda x: x == '.',
    DigitState.DIGIT2: lambda x: x.isdigit(),
    DigitState.E: lambda x: x == 'e',
    DigitState.NEGATIVE2: lambda x: x == '-',
    DigitState.DIGIT3: lambda x: x.isdigit(),
}


def parse_number(n):
    """
        Begin
    -   -> number
    \   /    \
      dot     e  -> -#
        \       \
        #2        #3 ()


    encode graph in adjacency list
    evolve state and get final state checking it if

    time: O(n)
    space: O(k) = O(1) b/c limited string size
    """
    state = DigitState.BEGIN
    for c in n:
        found = False
        for nxt in NEXT_STATES[state]:
            if STATE_VALIDATOR[nxt](c):
                state = nxt
                found = True
                break

        if not found:
            return False

    return state in [DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3]


for n in ('12.3', '12a'):
    print(parse_number(n))
