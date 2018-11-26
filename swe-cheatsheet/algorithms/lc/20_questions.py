from typing import List, Set


def processAnswer(answer: bool,
                  question: int,
                  objects: List[int],
                  table: List[List[int]]) -> Set[int]:
    return {oid for oid in objects if table[oid][question] == answer}


def nextQ(table: List[List[int]], objects: Set[int],
          questions: List[int]) -> int:
    questionIdx = None
    fromHalf = 0.5
    for qid in questions:
        diff = getRatio(table, objects, qid) - 0.5
        if diff < fromHalf:
            questionIdx = qid
            fromHalf = diff
            if not fromHalf:
                break

    return questions[questionIdx] if questionIdx is not None else -1


def getRatio(table: List[List[int]], objects, column: int) -> float:
    cnt = 0
    for i, row in enumerate(table):
        if i not in objects and row[column]:
            cnt += 1

    return cnt / len(table)


def getRatioLispy(table, column):
    return sum(filter(lambda cell: cell,
                      (table[row][column]
                       for row in range(len(table)))))


a = [[1, 1], [3, 1], [5, 0]]
print(getRatioLispy(a, 1))

