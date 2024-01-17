class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrows = len(board)
        ncols = len(board[0])
        not_surrounded = set()

        def dfs(row, col):
            if row not in range(nrows) or col not in range(ncols) or board[row][col] == "X" or (row, col) in not_surrounded:
                return

            not_surrounded.add((row, col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(nrows):
            for col in range(ncols):
                if (row == 0 or col == 0 or row == nrows-1 or col == ncols-1) and (row, col) not in not_surrounded and board[row][col] == "O":
                    dfs(row, col)

        for row in range(nrows):
            for col in range(ncols):
                if (row, col) not in not_surrounded:
                    board[row][col]="X"