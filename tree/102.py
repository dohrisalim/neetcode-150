class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        count = 0

        def bfs(count , root):
            if root == None :
                return 

            if len(result) <= count:
                result.append([])    
            
            result[count].append(root.val)
            count += 1
            bfs(count , root.left)
            bfs(count , root.right) 

        bfs(count , root)
        return result