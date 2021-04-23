# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # idea: traverse tree and assign (row, col) for each node
        # corner case
        if not root:
            return []
        # level order traversal
        nodes = [(root, 0, 0)] # (node, row, col)
        idx = 0
        while idx < len(nodes):
            node, row, col = nodes[idx]
            if node.left:
                nodes.append((node.left, row+1, col-1))
            if node.right:
                nodes.append((node.right, row+1, col+1))
            idx += 1
        # sort by col->row->val
        nodes.sort(key=lambda x: (x[2], x[1], x[0].val))
        # prepare result
        res = []
        last_col = None
        for node, _, col in nodes:
            if col != last_col:
                res.append([node.val])
            else:
                res[-1].append(node.val)
            last_col = col
        return res
        # Time: O(n), Space: O(n)

        # TODO: Read other solutions
