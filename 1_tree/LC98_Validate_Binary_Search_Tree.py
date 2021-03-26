# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # solution 1 - recursive with range
        def helper(node, l, h):
            if not node:
                return True
            if node.val <= l or node.val >= h:
                return False
            if not helper(node.left, l, node.val):
                return False
            if not helper(node.right, node.val, h):
                return False
            return True
        
        return helper(root, float('-inf'), float('inf'))
        # Time: O(n), Space: O(n)

        # solution 2 - iterative with range
        s = [(root, float('-inf'), float('inf'))]
        while s:
            node, l, h = s.pop()
            if node.val <= l or node.val >= h:
                return False
            if node.left:
                s.append((node.left, l, node.val))
            if node.right:
                s.append((node.right, node.val, h))
        
        return True
        # Time: O(n), Space: O(n)

        # solution 3 - recursive inorder
        self.prev = float('-inf')
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        
        return inorder(root)
        # Time: O(n), Space: O(n)

        # solution 4 - iterative inorder
        prev = float('-inf')
        s = []
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                node = node.right
        
        return True
        # Time: O(n), Space: O(n)
