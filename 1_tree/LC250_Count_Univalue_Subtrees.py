# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: recursive bottom-up
        # all leaf nodes are uni-value subtrees
        def helper(node):
            if node:
                lFlag, lVal = helper(node.left)
                rFlag, rVal = helper(node.right)
                if lFlag and rFlag:
                    if (lVal is None or node.val == lVal) and \
                       (rVal is None or node.val == rVal):
                        self.cnt += 1
                        return (True, node.val)
                    else:
                        return (False, node.val)
                else:
                    return (False, node.val)
            return (True, None)
        self.cnt = 0
        helper(root)
        return self.cnt
        # Time: O(n), Space: O(n)
