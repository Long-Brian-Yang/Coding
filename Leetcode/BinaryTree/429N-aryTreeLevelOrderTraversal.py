"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        # res is a list of lists, where each list contains the values of the nodes at a particular level
        def dfs(root, level):
            nonlocal res
            if not root:
                return
            
            if level == len(res):
                res.append([root.val])
            else:
                res[level].append(root.val)
            
            for child in root.children:
                dfs(child, level + 1)
        
        dfs(root, 0)
        return res