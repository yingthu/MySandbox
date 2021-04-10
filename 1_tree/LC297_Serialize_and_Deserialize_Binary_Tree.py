# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node, res):
            if node is None:
                res += '#,'
            else:
                res += str(node.val) + ','
                res = helper(node.left, res)
                res = helper(node.right, res)
            return res

        return helper(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(data_list):
            if data_list[0] == '#':
                data_list.pop(0)
                return None
            root = TreeNode(int(data_list.pop(0)))
            root.left = helper(data_list)
            root.right = helper(data_list)
            return root

        data_list = data.split(',')
        return helper(data_list)

    # Time: O(n), Space: O(n)

    # TODO: Analyze the problem in details

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))