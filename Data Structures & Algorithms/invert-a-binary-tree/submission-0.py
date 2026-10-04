# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(node):
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left != None:
                flip(node.left)
            if node.right != None:
                flip(node.right)       
        if root is not None:
            flip(root)
        return root
