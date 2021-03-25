class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea 1 - create all trees like LC95 and count, but TLE
        
        # idea 2 - can we use dynamic programming?
        # denote F(n) as the number of unique BSTs
        # F(0) = 1, F(1) = 1, F(2) = 2, F(3) = 5
        # we can partition 1...n to two parts: 1...k-1 and k+1...n
        # for 1...k-1, the number of unique BSTs are F(k-1)
        # for k+1...n, the number of unique BSTs should be equal 
        # to that of 1...n-k, i.e. F(n-k)
        # so we get F(n) = sum(F(k-1)*F(n-k)), k = 1...n
        F = [0] * (n+1)
        F[0], F[1] = 1, 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                F[i] += F[k-1] * F[i-k]
        
        return F[n]
        # Time: O(n^2), Space: O(n)