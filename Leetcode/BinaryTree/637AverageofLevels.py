# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        def dfs(root, level):
            nonlocal res
            if not root:
                return
            
            if level == len(res):
                res.append([root.val, 1])
            else:
                res[level][0] += root.val
                res[level][1] += 1
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        return [x / y for x, y in res]