from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        
        def dfs(node, path):
            path.append(str(node.val))
            
            if not node.left and not node.right:
                # leaf node, add the path
                result.append("->".join(path))
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)
            
            path.pop()  # backtrack
        
        dfs(root, [])
        return result