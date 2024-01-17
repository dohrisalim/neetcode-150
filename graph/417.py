class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev):
            if not ((0 <= r < rows) and (0 <= c < cols)):
                return 
            
            if (r, c) in visited or heights[r][c] < prev:
                return 
            
            visited.add((r, c))
            
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        return list(pacific & atlantic)