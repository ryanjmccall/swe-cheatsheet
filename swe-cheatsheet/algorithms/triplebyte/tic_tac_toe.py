
EMPTY = " "
P1 = "X"
P2 = "O"
OOB = -1


class Board:
    def __init__(self, size):
        self.human = P1
        self.cpu = P2
        self.b = [[EMPTY] * size for _ in range(size)]
        self.ways = self._computeWays(size)
        self.totalMoves = size * size
        self.moves = 0

    @staticmethod
    def _computeWays(size) -> list:
        leftDiag = []
        rightDiag = []
        ways = [leftDiag, rightDiag]
        for i in range(size):
            # horizontal ways
            ways.append([(i, j) for j in range(size)])

            # vertical ways
            ways.append([(j, i) for j in range(size)])

            leftDiag.append((i, i))
            rightDiag.append((i, size - 1 - i))

        return ways

    def addHumanMove(self):
        # ask for a move
        m = input("enter move: ")
        splits = m.strip().split(" ")
        if len(splits) != 2:
            print("bad move")
            return

        try:
            row = int(splits[0])
            col = int(splits[1])
        except ValueError:
            print("position must be two ints")
            return

        if row < 0 or row >= len(self.b) or col < 0 or col >= len(self.b):
            print("position out of bounds")
            return

        if self.b[row][col] != EMPTY:
            print("space already taken")
            return

        self.b[row][col] = self.human
        self.moves += 1

    def addCpuMove(self):
        for i, row in enumerate(self.b):
            for j, val in enumerate(row):
                if val == EMPTY:
                    self.b[i][j] = self.cpu
                    self.moves += 1
                    return

    def isWinner(self, player: str) -> bool:
        return any(all(self.b[i][j] == player for i, j in way)
                   for way in self.ways)

    def hasSpace(self) -> bool:
        return self.moves < self.totalMoves

    def print(self):
        print("\n".join("|".join(r) for r in self.b) + "\n")


def main():
    size = 3
    board = Board(size)
    while board.hasSpace():
        board.print()
        if board.moves % 2:
            player = board.cpu
            board.addCpuMove()
        else:
            player = board.human
            board.addHumanMove()

        if board.isWinner(player):
            print("%s won!" % player)
            break

    print("game over")
    board.print()


if __name__ == "__main__":
    main()
