from collections import deque


class Solution:
    def isSymmetricRecur(self, root) -> bool:
        if not root: return True

        def f(nl, nr):
            if not nl and not nr: return True
            if nl and nr:
                return nl.val == nr.val and f(nl.left, nr.right) and f(nl.right, nr.left)

            return False

        return f(root.left, root.right)

    def isSymmetric(self, root) -> bool:
        if not root: return True
        q = deque((root.left, root.right))
        while q:
            left, right = q.popleft(), q.popleft()
            if left and right:
                if left.val != right.val:
                    return False

                q.extend((left.left, right.right, left.right, right.left))

            elif left and not right or right and not left:
                return False

        return True
