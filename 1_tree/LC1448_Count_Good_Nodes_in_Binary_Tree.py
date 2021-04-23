# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        # idea: traverse tree while keeping max value in current path
        def helper(node, max_val):
            if node:
                if node.val >= max_val:
                    self.res += 1
                max_val = max(max_val, node.val)
                helper(node.left, max_val)
                helper(node.right, max_val)
        helper(root, float('-inf'))
        return self.res
        # Time: O(n), Space: O(n)