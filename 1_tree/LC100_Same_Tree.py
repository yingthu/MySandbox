# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # solution 1 - recursive
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right) and \
               p.val == q.val
        # Time: O(n), Space: O(n)

        # solution 2 - iterative
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop(0)
            if n1 and n2 and n1.val == n2.val:
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
            elif n1 or n2:
                return False
        return True
        # Time: O(n), Space: O(n)
