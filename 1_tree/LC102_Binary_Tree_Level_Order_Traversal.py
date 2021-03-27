# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        cnt = len(queue)
        while queue:
            curLevel = []
            for i in range(cnt):
                node = queue.pop(0)
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cnt = len(queue)
            res.append(curLevel)
        return res
        # Time: O(n), Space: O(n)

        # TODO: Use a recursive method
