# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # solution 1 - bfs
        if not root:
            return False
        queue = [(root, 0)]
        while queue:
            cnt = len(queue)
            for _ in range(cnt):
                node, curSum = queue.pop(0)
                newSum = curSum + node.val
                # sum == targetSum and leaf node
                if newSum == targetSum and not node.left and not node.right:
                    return True
                if node.left:
                    queue.append((node.left, newSum))
                if node.right:
                    queue.append((node.right, newSum))
        return False
        # Time: O(n), Space: O(n)
        
        # solution 2 - recursive dfs
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or \
               self.hasPathSum(root.right, targetSum-root.val)
        # Time: O(n), Space: O(n)
        
        # solution 3 - iterative dfs
        # TODO: why first push right node to stack?
