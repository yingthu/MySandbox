# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # idea: feel like it would be more straightforward
        # if we use a recursive method
        if root and root.left:
            newRoot = self.upsideDownBinaryTree(root.left)
            root.left.right = root
            root.left.left = root.right
            root.left = None
            root.right = None
            return newRoot
        return root
        # Time: O(n), Space: O(n)
