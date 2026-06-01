# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.right)
                queue.append(node.left)
                node.right, node.left = node.left, node.right
        return root