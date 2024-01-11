class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        def dfs(opened, closed, s):
            if len(s) == n * 2:
                result.append(s)
                return None

            if opened < n:
                dfs(opened + 1, closed, s + '(')

            if closed < opened:
                dfs(opened, closed + 1, s + ')')

        result = list()
        dfs(0, 0, '')
        return result
            