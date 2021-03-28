# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # solution 1 - iterative
        # idea: do the normal level order traversal
        # but append results to the front
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            cntLevel = len(queue)
            curLevel = []
            for _ in range(cntLevel):
                node = queue.pop(0)
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res = [curLevel] + res
        return res
        # Time: O(n), Space: O(n)

        # solution 2 - recursive for fun
        if not root:
            return []
        res = {}
        # let's write a recursive solution for fun
        def recursiveHelper(node, level):
            if level in res:
                res[level].append(node.val)
            else:
                res[level] = [node.val]
            # this order guarantees left to right for each level
            if node.left:
                recursiveHelper(node.left, level+1)
            if node.right:
                recursiveHelper(node.right, level+1)
        recursiveHelper(root, 0)
        # collect output
        return [res[k] for k in sorted(res, reverse=True)]
        # Time: O(n), Space: O(n)
