"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        def helper(root: 'Node', level: int):
            if not root: return
            nonlocal ans
            ans = max(ans,level)
            for i in root.children:
                helper(i,level+1)
        helper(root,1)
        return ans
        