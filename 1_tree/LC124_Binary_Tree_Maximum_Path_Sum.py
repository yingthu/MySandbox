# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # TODO: Digest and generalize this problem
        self.maxSum = float('-inf')
        def helper(node):
            if not node:
                return 0
            # Check left sub-tree and right sub-tree
            # max(_, 0) is very important!
            leftMax = max(helper(node.left), 0)
            rightMax = max(helper(node.right), 0)
            # New path that contains node
            newSum = leftMax + node.val + rightMax
            self.maxSum = max(self.maxSum, newSum)
            # Continue current path
            return node.val + max(leftMax, rightMax)
        helper(root)
        return self.maxSum
        # Time: O(N), Space: O(H)
