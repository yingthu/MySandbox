# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # idea: do level order traversal and record
        # right most node of each level
        if not root:
            return []
        res = []
        q = [root]
        while q:
            cnt = len(q)
            for i in range(cnt):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == cnt-1:
                    res.append(node.val)
        return res
        # Time: O(N), Space: O(W)

        # TODO: Other methods like DFS?
