class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def DFS(root):
            if not root:
                ans.append("N")
                return

            ans.append(str(root.val))
            DFS(root.left)
            DFS(root.right)

        DFS(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value = data.split(",")
        self.index = 0

        def DFS():
            if value[self.index] == "N":
                self.index += 1
                return None

            root = TreeNode(int(value[self.index]))
            self.index += 1
            root.left = DFS()
            root.right = DFS()
            return root

        return DFS()