# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Average time: O(log(n)) space: O(log(n))
        Worst time: O(n) space: O(n)
        """
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

        return self

    def contains(self, value):
        cur = self
        while cur:
            if cur.value == value:
                return True

            if cur.value < value:
                cur = cur.right
            else:
                cur = cur.left

        return False


    def remove(self, value, parent=None):
        if self.value > value:
            if self.left:
                self.left.remove(value, self)
                return self

        if self.value < value:
            if self.right:
                self.right.remove(value, self)
                return self

        # found value
        if self.left and self.right:
            self.value = self.right.get_min_value()
            self.right.remove(self.value, self)
            return self

        if not parent:
            node = self.left or self.right
            if node:
                self.value = node.value
                self.left = node.left
                self.right = node.right
            return self

        if parent.left == self:
            parent.left = self.left if self.left else self.right
            return self

        if parent.right == self:
            parent.right = self.right if self.right else self.left
            return self


        return self


    def get_min_value(self):
        return self.left.get_min_value() if self.left else self.value



# Iterative solution almost works

    # def remove(self, value, parent=None):
    #     prev, cur = None, self
    #     while cur and cur.value != value:
    #         prev = cur
    #         if value < cur.value:
    #             cur = cur.left
    #         elif value > cur.value:
    #             cur = cur.right
    #
    #     if not prev:
    #         return self._remove_root(cur)
    #
    #     if prev.left == cur:
    #         prev.left = self._remove_root(cur)
    #     else:
    #         prev.right = self._remove_root(cur)
    #
    #     return self
    #
    # def _remove_root(self, root):
    #     if not root:
    #         return None
    #     if not root.left:
    #         return root.right
    #     if not root.right:
    #         return root.left
    #
    #     prev, cur = None, root.right
    #     while cur.left:
    #         prev, cur = cur, cur.left
    #
    #     cur.left = root.left
    #     if root.right != cur:
    #         prev.left = cur.right
    #         cur.right = root.right
    #
    #     return cur