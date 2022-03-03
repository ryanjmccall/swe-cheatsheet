from typing import List


def moveElementToEnd(array: List[int], toMove: int):
    i, j = 0, len(array) - 1
    while i < j:
        while j >= 0 and array[j] == toMove:
            j -= 1
            if j <= i:
                break

        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]

        i += 1

    return array



def main():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    moveElementToEnd(array, 2)
    print(array)


main()

