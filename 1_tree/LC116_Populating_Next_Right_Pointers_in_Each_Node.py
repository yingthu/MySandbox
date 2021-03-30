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
        # idea: use level order traversal
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

        # follow-up: only use constant extra space
        # idea: use next pointers from level k for level k+1
        # there are 2 types of next pointer connections
        # 1) they have a common parent
        # 2) they have a common grandparent
        # treat each established level as a linked list
        if not root:
            return root
        
        head = root
        while head.left:
            node = head
            while node:
                # 1) nodes with common parent
                node.left.next = node.right
                # 2) nodes with common grandparent
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            # next level
            head = head.left
        
        return root
        # Time: O(n), Space: O(1)
