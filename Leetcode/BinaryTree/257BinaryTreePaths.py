# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                path += str(node.val)
                paths.append(path)
                return
            path += str(node.val) + '->'
            dfs(node.left, path)
            dfs(node.right, path)
        
        paths = []
        dfs(root, '')
        
        return paths