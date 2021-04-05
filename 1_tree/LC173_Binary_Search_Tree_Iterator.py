# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # record inorder traversal of BST
        self.inorder = []
        def helper(node):
            if node:
                helper(node.left)
                self.inorder.append(node.val)
                helper(node.right)
        helper(root)
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        # always valid next() calls
        val = self.inorder[self.idx]
        self.idx += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.inorder)

    # TODO: Instead of flattening the BST, try controlled recursion

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()