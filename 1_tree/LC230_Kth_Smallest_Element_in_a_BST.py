# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # idea: flatten the BST
        self.elements = []
        # inorder traversal
        def helper(node):
            if node:
                helper(node.left)
                self.elements.append(node.val)
                helper(node.right)
        helper(root)
        return self.elements[k-1]
        # Time: O(n), Space: O(n)

        # TODO: Any other solution that's more elegant?
