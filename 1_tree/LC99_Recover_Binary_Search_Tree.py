
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # solution 1: step by step
        # inorder traversal of input tree should be an almost sorted array
        t_res = []
        def inorder(node):
            if node:
                inorder(node.left)
                t_res.append(node.val)
                inorder(node.right)
        inorder(root)
        
        # check sapped values in traverse_res
        val_1, val_2 = None, None
        for i in range(len(t_res)-1):
            if t_res[i+1] < t_res[i]:
                if val_1 is None:
                    val_1 = t_res[i]
                    val_2 = t_res[i+1] # cover adjacent swap
                else:
                    val_2 = t_res[i+1]
                    break
        
        # recover BST
        def traverse(node, remain=2):
            if not node:
                return
            if node.val == val_1:
                node.val = val_2
                remain -= 1
            elif node.val == val_2:
                node.val = val_1
                remain -= 1
            if remain == 0:
                return
            traverse(node.left, remain)
            traverse(node.right, remain)
        traverse(root)
        # Time: O(n), Space: O(n)

        # solution 2: try merging first 2 steps, recursive
        self.precedent, self.node_1, self.node_2 = None, None, None
        def bugFinder(node):
            if node:
                bugFinder(node.left)
                if self.precedent and node.val < self.precedent.val:
                    if self.node_1 is None:
                        self.node_1 = self.precedent
                        self.node_2 = node
                    else:
                        self.node_2 = node
                        return
                self.precedent = node
                bugFinder(node.right)
        bugFinder(root)
        # found, now swap
        self.node_1.val, self.node_2.val = self.node_2.val, self.node_1.val
        # Time: O(n), Space: O(n)

        # solution 3: try merging first 2 steps, iterative
        s, precedent, n1, n2 = [], None, None, None
        node = root
        while node or len(s) > 0:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if precedent and node.val < precedent.val:
                    if n1 is None:
                        n1 = precedent
                        n2 = node
                    else:
                        n2 = node
                precedent = node
                node = node.right
        n1.val, n2.val = n2.val, n1.val
        # Time: O(n), Space: O(n)

        # TODO: solution 4: use Morris Traversal
