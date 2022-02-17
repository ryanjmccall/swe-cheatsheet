from typing import List


def distribute_bonus(a: List[int], default_bonus: int = 1) -> List[int]:
    """Computes bonuses based on given employee performance scores.

    The employee bonus multiplier of employee i is 1 more than
    the max of the neighboring employees if they are defined.

    let n = employees
    time: O(n)
    space: O(n)

    :param default_bonus:
    :param a: Employee performances
    :return: Employee bonus multipliers
    """
    bonus = [default_bonus] * len(a)
    for i in range(len(a)):
        if i > 0 and a[i - 1] < a[i]:
            bonus[i] = max(bonus[i], a[i - 1] + 1)
        if i < len(a) - 1 and a[i] > a[i + 1]:
            bonus[i] = max(bonus[i], a[i + 1] + 1)

    return bonus


print(distribute_bonus([1, 2, 3, 4, 3, 1]))
