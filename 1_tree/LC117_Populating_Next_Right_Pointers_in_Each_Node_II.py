"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # idea: level order traversal should still work
        if not root:
            return root
        q = [root]
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(q)-1):
                q[i].next = q[i+1]
        return root
        # Time: O(n), Space: O(n)

        # Follow-up: constant extra space
        # idea: similar to LC116, but head of each level is not as obvious
        if not root:
            return root
        # first node for each level
        head = root
        while head:
            node, head = head, None # clear head for next level
            n1, n2 = None, None
            while node:
                if node.left:
                    if not n1:
                        head = node.left # head for next level
                        n1 = node.left
                    else:
                        n2 = node.left
                        n1.next = n2
                        n1, n2 = n2, None
                if node.right:
                    if not n1:
                        head = node.right # head for next level
                        n1 = node.right
                    else:
                        n2 = node.right
                        n1.next = n2
                        n1, n2 = n2, None
                node = node.next

        return root
        # Time: O(n), Space: O(1)
