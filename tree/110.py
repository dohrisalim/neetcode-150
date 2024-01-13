class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:  return 0
            leftheight, rightheight = height(root.left), height(root.right)
            if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
            return max(leftheight, rightheight) + 1
            
        return (height(root) >= 0)