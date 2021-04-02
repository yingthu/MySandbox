# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # corner case
        if not root:
            return []
        # iterative solution
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res
        # Time: O(n), Space: O(n)

        # TODO 1: Recursive
        # TODO 2: Morris traversal
        # TODO 3: Go over common traveral methods for
        # tree preorder/inorder/postorder/levelorder
