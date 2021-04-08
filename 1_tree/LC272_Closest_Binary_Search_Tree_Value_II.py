# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # idea 1 - flatten the BST into an array and
        # sort by distances to target
        self.vals = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.vals.append(node.val)
                inorder(node.right)
        inorder(root)
        self.vals.sort(key=lambda x: abs(x-target))
        return self.vals[:k]
        # Time: O(nlogn), Space: O(n)

        # idea 2 - keep a sorted list of k closest values
        self.kvals = []
        def helper(node, target, k):
            if node:
                if len(self.kvals) < k or abs(node.val - target) < abs(self.kvals[-1] - target):
                    i = 0
                    while i < len(self.kvals):
                        if abs(self.kvals[i] - target) > abs(node.val - target):
                            break
                        i += 1
                    self.kvals.insert(i, node.val)
                    self.kvals = self.kvals[:k]
                helper(node.left, target, k)
                helper(node.right, target, k)

        helper(root, target, k)
        return self.kvals
        # Time: O(nk), Space: O(n)
        # Super slow...

        # idea 3 - can we use any data structure to optimize the insertion part?
        # yes we can use a priority queue
        import heapq
        self.kvals = []
        def helper(node, target, k):
            if node:
                heapq.heappush(self.kvals, (-abs(node.val - target), node.val))
                if len(self.kvals) > k:
                    heapq.heappop(self.kvals)
                helper(node.left, target, k)
                helper(node.right, target, k)

        helper(root, target, k)
        return [x for _, x in self.kvals]
        # Time: O(nlogk), Space: O(n)

        # TODO: Dive deeper into heapq and check if there are better solutions
