class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return [
            ["." * i + "Q" + "." * (n - i - 1) for i in p]
            for p in permutations(range(n))
            if len(set(map(lambda z: z[0] - z[1], enumerate(p))))
            == len(set(map(lambda z: z[0] + z[1], enumerate(p))))
            == n
        ]