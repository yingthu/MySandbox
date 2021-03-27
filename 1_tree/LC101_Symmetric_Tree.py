# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # solution 1 - recursive
        if not root:
            return True
        def checkTree(n1, n2):
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (n2 and not n1):
                return False
            if n1.val != n2.val:
                return False
            return checkTree(n1.left, n2.right) and checkTree(n1.right, n2.left)
        
        return checkTree(root.left, root.right)
        # Time: O(n), Space: O(n)
        
        # solution 2 - iterative
        if not root:
            return True
        s1, s2 = [root.left], [root.right]
        while len(s1) > 0 and len(s2) > 0:
            n1, n2 = s1.pop(), s2.pop()
            if (n1 and not n2) or (n2 and not n1):
                return False
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                s1.append(n1.left)
                s1.append(n1.right)
                s2.append(n2.right)
                s2.append(n2.left)
        
        return True
        # Time: O(n), Space: O(n)
