class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])
			
            return root