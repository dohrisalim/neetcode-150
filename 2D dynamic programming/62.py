class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0 or m == 0 :
            return 0

        ans = [[0] * n for _ in range(m)]

        for i in range(n):
            ans[0][i] = 1

        for i in range(m):
            ans[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]

        return ans[m-1][n-1]