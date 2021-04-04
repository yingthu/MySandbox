# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # solution 1 - recursive
        def helper(node, res):
            if node:
                helper(node.left, res)
                helper(node.right, res)
                res.append(node.val)
        res = []
        helper(root, res)
        return res
        # Time: O(n), Space: O(n)

        # solution 2 - iterative
        # root->right->left and then reverse
        if not root:
            return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            if node:
                res.append(node.val)
                s.append(node.left)
                s.append(node.right)
        return res[::-1]
        # Time: O(n), Space: O(n)

        # solution 3 - iterative
        # use a flag to mark whether current node's immediate
        # children are visited or not
        res = []
        s = [(root, False)]
        while s:
            node, visited = s.pop()
            if node:
                if visited:
                    # add to result
                    res.append(node.val)
                else:
                    # post-order
                    s.append((node, True))
                    s.append((node.right, False))
                    s.append((node.left, False))
        return res
        # Time: O(n), Space: O(n)
