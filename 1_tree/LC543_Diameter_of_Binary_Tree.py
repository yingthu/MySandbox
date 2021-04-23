# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: try every node as the highest-level node in the
        # longest path and keep track of the maximum length from
        # leaf to the current node
        self.maxlen = 0
        # find max length that goes from leaf to current node
        def helper(node):
            if not node:
                return -1
            left = helper(node.left)
            right = helper(node.right)
            newlen = left + right + 2
            self.maxlen = max(self.maxlen, newlen)
            return 1 + max(left, right)
        helper(root)
        return self.maxlen
        # Time: O(n), Space: O(n)
