# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # generate BST with values from start to end
        def treeHelper(start, end):
            # terminating condition
            if start > end:
                return [None]
            trees = []
            # partition
            for pVal in range(start, end+1):
                # generate left trees
                leftTrees = treeHelper(start, pVal-1)
                rightTrees = treeHelper(pVal+1, end)
                # connect to parent node
                for l in leftTrees:
                    for r in rightTrees:
                        pNode = TreeNode(pVal)
                        pNode.left = l
                        pNode.right = r
                        trees.append(pNode)
            # return
            return trees
        
        return treeHelper(1, n)
        # Time: TODO, Space: TODO