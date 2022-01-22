

class Soln(object):

    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        # go left <
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)

            force[i] -= f

        for i in range(N):
            if force[i] > 0:
                force[i] = 'R'
            elif force[i] < 0:
                force[i] = 'L'
            else:
                force[i] = '.'

        return ''.join(force)


print(Soln().pushDominoes(dominoes=".L.R...LR..L.."))
