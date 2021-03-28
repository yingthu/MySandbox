# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # idea: last item in postorder is root,
        # again use inorder to split left and 
        # right sub-trees
        # pay attention to construction order though
        if not inorder:
            return None
        rootVal = postorder.pop()
        idx = inorder.index(rootVal)
        root = TreeNode(rootVal)
        # construct right sub-tree first
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root
        # Time: O(n), Space: O(n)
