# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n = root
        while n is not None:
            if n.val == val:
                return n
            elif val < n.val:
                n = n.left
            else:
                n = n.right
        return None