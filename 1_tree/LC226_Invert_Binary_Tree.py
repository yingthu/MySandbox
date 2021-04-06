# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # solution 1 - recursive
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        # Time: O(n), Space: O(n)

        # solution 2 - iterative
        if not root:
            return root
        queue = [root]
        while queue:
            cnt = len(queue)
            for _ in range(cnt):
                node = queue.pop(0)
                # invert
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        # Time: O(n), Space: O(n)
