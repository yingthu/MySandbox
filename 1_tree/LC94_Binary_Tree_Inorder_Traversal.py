# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # solution 1 - recursive
        def traverseHelper(node, result):
            if node.left:
                traverseHelper(node.left, result)
            result.append(node.val)
            if node.right:
                traverseHelper(node.right, result)
        
        result = []
        if root:
            traverseHelper(root, result)
        return result
        # Time: O(n), Space: O(n)

        # solution 2 - iterative
        # 1 - create a stack s
        # 2 - initialize current node as root
        # 3 - push current node to s and set cur_node = 
        #     cur_node.left until cud_node is None
        # 4 - if not cur_node and s is non-empty
        #   - pop item from s
        #   - add popped item to result, set cur_node = 
        #     popped_node.right
        #   - go to 3
        # 5 - if cur_node is None and s is empty, done.
        result = []
        s = []
        cur_node = root
        while len(s) > 0 or cur_node:
            if cur_node:
                s.append(cur_node)
                cur_node = cur_node.left
            else:
                popped_node = s.pop()
                result.append(popped_node.val)
                cur_node = popped_node.right
        return result
        # Time: O(n), Space: O(n)

        # TODO: Use Morris Traversal (Threaded Binary Tree)