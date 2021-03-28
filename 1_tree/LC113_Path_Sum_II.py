# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # solution 1 - bfs
        if not root:
            return []
        res = []
        queue = [(root, 0, [])]
        while queue:
            cnt = len(queue)
            for _ in range(cnt):
                node, curSum, curPath = queue.pop(0)
                newSum = curSum + node.val
                newPath = curPath + [node.val]
                if newSum == targetSum and not node.left and not node.right:
                    res.append(newPath)
                if node.left:
                    queue.append((node.left, newSum, newPath))
                if node.right:
                    queue.append((node.right, newSum, newPath))
        return res
        # Time: O(n), Space: O(n)

        # solution 2 - recursive dfs
        if not root:
            return []
        res = []
        def recursiveHelper(node, targetSum, curPath):
            newPath = curPath + [node.val]
            if node.val == targetSum and not node.left and not node.right:
                res.append(newPath)
            if node.left:
                recursiveHelper(node.left, targetSum-node.val, newPath)
            if node.right:
                recursiveHelper(node.right, targetSum-node.val, newPath)
        recursiveHelper(root, targetSum, [])
        return res
