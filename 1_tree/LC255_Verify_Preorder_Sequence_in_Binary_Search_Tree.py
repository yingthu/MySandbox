class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # idea: try putting values in BST and check
        # solution 1 - TLE however
        def helper(preorder, threshold, left):
            if not preorder:
                return True
            val = preorder[0]
            if left and max(preorder) > threshold:
                return False
            if not left and min(preorder) < threshold:
                return False
            i = 1
            while i < len(preorder):
                if preorder[i] > val:
                    break
                i += 1
            return helper(preorder[1:i], val, True) \
               and helper(preorder[i:], val, False)
        return helper(preorder, float('inf'), True)
        # Time: O(n!), Space: O(n)

        # solution 2 - each time we encounter preorder[i] > preorder[i-1],
        # we're going to the right sub-tree of some node and this is the
        # time we should update lower bound for future nodes: future nodes
        # should at least be bigger than the current parent.
        low = float('-inf')
        s = []
        for p in preorder:
            if p < low:
                return False
            if not s or p < s[-1]:
                s.append(p)
            else:
                while s and p > s[-1]:
                    low = s.pop()
                s.append(p)
        return True
        # Time: O(n), Space: O(n)

        # TODO: O(1) space?
