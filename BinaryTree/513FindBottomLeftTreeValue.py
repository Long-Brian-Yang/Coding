# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if not node:
                return
            
            if level > self.max_level:
                self.max_level = level
                self.leftmost = node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        self.max_level = 0
        self.leftmost = root.val
        dfs(root, 0)
        
        return self.leftmost


print(Solution().findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))