# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: we can solve it by simply traversing
        # all tree nodes, but this requires O(n)
        # time complexity. As it's a complete tree,
        # we only need to 1) get tree depth, 2) count
        # number of nodes at last level
        
        # corner case
        if not root:
            return 0
        
        # get depth of tree
        depth = 0
        node = root
        while node:
            depth += 1
            node = node.left
        
        # count from first depth-1 levels
        res = 2 ** (depth-1) - 1
        
        # number of nodes at last level could range
        # from 1 to 2^(depth-1)
        # check if node exists using binary search
        def isNodeExist(node, depth, idx):
            start, end = 0, 2**(depth-1)-1
            for i in range(1, depth):
                pivot = start + (end - start) // 2
                if idx <= pivot:
                    node = node.left
                    end = pivot
                else:
                    node = node.right
                    start = pivot + 1
            return node is not None
        
        start, end = 0, 2**(depth-1)-1
        while start <= end:
            pivot = start + (end - start) // 2
            if isNodeExist(root, depth, pivot):
                start = pivot + 1
            else:
                end = pivot - 1
        
        res += start
        return res
        # Time: O(H) - get depth, O(logW*logW) - check node exists
        # Space: O(1)
