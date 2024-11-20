class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(root):
            nonlocal res
            if not root:
                return
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res