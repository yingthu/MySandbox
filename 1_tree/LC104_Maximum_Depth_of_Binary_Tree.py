# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: DFS should be the simplest
        # solution 1 - DFS
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # Time: O(n), Space: O(n)

        # solution 2 - BFS
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            cnt = len(queue)
            for _ in range(cnt):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
        # Time: O(n), Space: O(n)
