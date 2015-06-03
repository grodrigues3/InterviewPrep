import math
import pdb

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        
        values = range(1,n+1)
        perm = []
        self.getPermHelper(values, k, perm)
        toRet = "".join([str(c) for c in perm])
        return toRet
    
    def getPermHelper(self, values, k, perm):
        n_1 = len(values) - 1
        n_1_fact = 1
        for n in range(1,n_1+1):
            n_1_fact *= n
        setInd = math.ceil(k / n_1_fact) - 1
        setInd = int(setInd)
        firstDig = values[setInd]
        perm += [firstDig]
        values.remove(firstDig)
        if values == []:
            return perm
        newK = k%n_1_fact
        if newK == 0:
            newK = n_1_fact
        return self.getPermHelper(values,newK, perm)



S = Solution()
print S.getPermutation(9,10000)
