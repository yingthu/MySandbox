# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # idea: traverse tree
        def dfs(node, path):
            if node:
                # leaf node
                if not node.left and not node.right:
                    self.paths.append("->".join(str(x) for x in path + [node.val]))
                    return
                dfs(node.left, path + [node.val])
                dfs(node.right, path + [node.val])
        self.paths = []
        dfs(root, [])
        return self.paths
        # Time: O(n), Space: O(n)
