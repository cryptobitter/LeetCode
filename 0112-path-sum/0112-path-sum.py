# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node , Cursum):
            if node is None :
                return False
            Cursum += node.val
            if node.left is None and node.right is None:
                return Cursum == targetSum
            
            return dfs(node.left,Cursum) or dfs(node.right , Cursum)
        
        return dfs(root, 0)
        