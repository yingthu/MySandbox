# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # idea: recursive + isTreeEqual to check if t is equal to subtree of s
        def isTreeEqual(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val \
               and isTreeEqual(s.left, t.left) \
               and isTreeEqual(s.right, t.right)
        
        return isTreeEqual(s, t) \
            or (s.left and self.isSubtree(s.left, t)) \
            or (s.right and self.isSubtree(s.right, t))
        # Time: O(mn), Space: O(n)
