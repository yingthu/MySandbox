# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # idea 1: check which sub-tree that p, q belong to
        # solution TLD
        if root.val == p.val or root.val == q.val:
            return root
        # check if node in tree
        def isInTree(root, node):
            if root:
                if root.val == node.val:
                    return True
                return isInTree(root.left, node) or isInTree(root.right, node)
            return False
        # check p, q in left or right sub-tree
        pInLeft = isInTree(root.left, p)
        qInRight = isInTree(root.right, q)
        if (pInLeft and qInRight) or (not pInLeft and not qInRight):
            return root
        if pInLeft and not qInRight:
            return self.lowestCommonAncestor(root.left, p, q)
        if not pInLeft and qInRight:
            return self.lowestCommonAncestor(root.right, p, q)
        # Time: O(n!), Space: O(n)

        # idea 2: find path to p and q
        def findPath(root, path, node):
            if root:
                path.append(root)
                if root.val == node.val:
                    return True
                if findPath(root.left, path, node) or findPath(root.right, path, node):
                    return True
                # remove current root if node not in sub-tree
                path.pop()
            return False
        
        path_p, path_q = [], []
        findPath(root, path_p, p)
        findPath(root, path_q, q)
        i = 0
        while i < len(path_p) and i < len(path_q):
            if path_p[i].val != path_q[i].val:
                break
            i += 1
        return path_p[i-1]
        # Time: O(n), Space: O(n)

        # idea 3: similar to idea 1, but the method itself can already check
        # whether at least one node is in a sub-tree or not as we check for
        # p == node or q == node at the beginning.
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca
        # Time: O(N), Space: O(H)

        # TODO: Read solution and discussion
