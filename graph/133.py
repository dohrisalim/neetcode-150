from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        nodes = []
        seen = [0]* 101
        nodes.append(0)
        for i in range(100):
            nodes.append(Node(i+1))
        def dfs(n,cp):
            if seen[n.val] == 1:
                return
            seen[n.val] = 1
            if n.neighbors == None:
                cp.neighbors = None
                return

            for i in n.neighbors:
                cp.neighbors.append(nodes[i.val])
                dfs(i,nodes[i.val])
        dfs(node,nodes[node.val])

        return nodes[node.val]