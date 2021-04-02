# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: dfs and keep track of current number
        self.sum = 0
        def dfs(node, num):
            if not node:
                return 0
            # update number
            num = num * 10 + node.val
            # recursion
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)
            # leaf node
            if not node.left and not node.right:
                self.sum += num
        dfs(root, 0)
        return self.sum
        # Time: O(N), Space: O(H)

        # TODO 1: Write iterative method using stack
        # TODO 2: Use Morris Traversal (constant space)
