# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # solution 1 - iterative
        # bfs should be faster
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            cnt = len(queue)
            for _ in range(cnt):
                node = queue.pop(0)
                # leaf node
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # Time: O(n), Space: O(n)

        # solution 2 - recursive
        # this is actually dfs
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # Time: O(n), Space: O(n)
