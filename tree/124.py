class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.findMaxSum(root)
        return self.ans

    def findMaxSum(self,node):
        if not node:
            return 0
        
        leftMax = max(0,self.findMaxSum(node.left))
        rightMax = max(self.findMaxSum(node.right),0)
		
        self.ans = max(self.ans,leftMax + rightMax + node.val) 
        return max(leftMax, rightMax) + node.val