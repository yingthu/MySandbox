# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # idea 1 - flatten the tree to a sorted array
        self.nodes = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.nodes.append(node)
                inorder(node.right)

        inorder(root)
        for i in range(len(self.nodes)):
            if self.nodes[i].val == p.val:
                break
        return self.nodes[i + 1] if i + 1 < len(self.nodes) else None
        # Time: O(n), Space: O(n)

        # idea 2 - search for node in BST and keep track of
        # successor candidates
        if not root:
            return None
        # p in left sub-tree,
        # successor in left sub-tree or is root
        if p.val < root.val:
            lres = self.inorderSuccessor(root.left, p)
            if lres and lres.val < root.val:
                return lres
            else:
                return root
        # p is root or in right sub-tree,
        # successor in right sub-tree or is None
        if p.val >= root.val:
            rres = self.inorderSuccessor(root.right, p)
            return rres
        # Time: O(logn), Space: O(n)

        # TODO: Dive deeper
