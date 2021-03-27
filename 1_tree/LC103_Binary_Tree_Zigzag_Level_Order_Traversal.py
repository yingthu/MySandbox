# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # idea: level order traversal while maintaining direction
        if not root:
            return []
        res = []
        queue = [root]
        direction = 1
        while queue:
            cnt = len(queue)
            curLevel = []
            for i in range(cnt):
                if direction == 1:
                    node = queue.pop(0)
                    curLevel.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    curLevel.append(node.val)
                    if node.right:
                        queue = [node.right] + queue # important
                    if node.left:
                        queue = [node.left] + queue
            res.append(curLevel)
            direction = -direction
        return res
        # Time: O(n), Space: O(n)

        # TODO: Use DFS
