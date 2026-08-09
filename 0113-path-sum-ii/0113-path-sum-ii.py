# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def dfs(node,Cursum,cur_path):
            if not node :
                return 

            cur_path.append(node.val)
            Cursum += node.val

            if not node.left and not node.right :
                if Cursum == targetSum:
                    result.append(list(cur_path))
            else:
                dfs(node.left,Cursum,cur_path) 
                dfs(node.right,Cursum,cur_path)
            
            cur_path.pop()

        dfs(root,0,[])
        return result