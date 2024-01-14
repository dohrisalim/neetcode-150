class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        prev_max=float("-inf")

        def dfs(node, prev_max, result):
            if not node:
                return

            if prev_max<=node.val:
                result.append(node.val)

            prev_max = max(node.val, prev_max)

            if node.left:
                dfs(node.left, prev_max, result)
            
            if node.right:
                dfs(node.right, prev_max, result)
        
        dfs(root, prev_max, result)
        return len(result)