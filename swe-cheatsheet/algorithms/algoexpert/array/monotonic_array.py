def isMonotonic(array):
    if not array:
        return True

    has_increase = False
    has_decrease = False
    prev = array[0]
    for v in array[1:]:
        if prev < v:
            has_increase = True
        elif prev > v:
            has_decrease = True
        prev = v

    return not (has_increase and has_decrease)


def findKthLargestValueInBst(tree, k):
    order = []

    def traverse(n):
        if n.left:
            traverse(n.left)

        order.append(n.value)
        if n.right:
            traverse(n.right)

    traverse(tree)


    return order[-k - 1]