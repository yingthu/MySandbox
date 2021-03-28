# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # analysis: first node in preorder -> root
        # locate root idx in inorder
        # inorder[:idx] belongs to left sub-tree
        # inorder[idx+1:] belongs to right sub-tree
        if not preorder:
            return None
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        idx = inorder.index(rootVal)
        root.left = self.buildTree(preorder[:idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx:], inorder[idx+1:])
        return root
        # Time: O(n), Space: O(n)
