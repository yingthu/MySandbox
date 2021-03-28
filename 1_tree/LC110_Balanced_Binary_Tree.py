# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # solution 1 - bottom-up
        def getHeight(node):
            if not node:
                return 0, True
            lHeight, lBalanced = getHeight(node.left)
            if not lBalanced:
                return -1, False
            rHeight, rBalanced = getHeight(node.right)
            if not rBalanced:
                return -1, False
            return max(lHeight, rHeight) + 1, abs(lHeight-rHeight) <= 1

        return getHeight(root)[1]
        # Time: O(n), Space: O(n)

        # solution 2 - top-bottom
        # this involves some repeated calls to get sub-tree height
        # TODO: induct the time complexity by hand
        # logn for getting height as it's a balanced tree
        # Time: O(nlogn), Space: O(n)
