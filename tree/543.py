class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if root == None:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0] , 2 + left + right)

            return 1 + max(left , right)

        dfs(root)
        return result[0]