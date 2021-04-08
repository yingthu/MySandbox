# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = float('inf')
        def helper(node, target):
            if node:
                # node.val == target
                if node.val == target:
                    self.closest = node.val
                    return
                # update closest
                if abs(node.val - target) < abs(self.closest - target):
                    self.closest = node.val
                # choose BST branch
                if target < node.val:
                    helper(node.left, target)
                else:
                    helper(node.right, target)
        helper(root, target)
        return self.closest
        # Time: O(n), Space: O(n)
