

class S:

    def reconstruct_q(self, q):
        q.sort(key=lambda x: (-x[0], x[1]))
        print(q)
        result = []
        for v in q:
            result.insert(v[1], v)

        return result


print(S().reconstruct_q(q=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
