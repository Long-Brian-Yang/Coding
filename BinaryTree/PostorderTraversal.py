class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res