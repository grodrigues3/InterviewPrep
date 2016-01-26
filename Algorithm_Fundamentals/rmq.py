from math import log
import pdb, traceback
test = range(10)
n = len(test)

def log2(a):
    return int(log(a)/log(2))

test = [2,4,3,1,6,7,8,9,1,7]

numPows = log2(n) # log2(20) = 4
A = {}

for startInd in range(n):
    A[(startInd,0)] = startInd


for ll in range(1, numPows+1):
    theLen = 2**ll
    for startInd in range(n-theLen+1):
            a = A[(startInd, ll-1)]
            b = A[(startInd + theLen/2, ll-1)]
            if test[a] <= test[b]:
                A[(startInd, ll)] = a
            else:
                A[(startInd, ll)] = b

for i in range(20):
    for j in range(numPows+1):
        if i + 2**j <= n:
            pass

        


def rmq(a, b):
    if a == b:
        return a
    ll = log2(b-a+1)
    first = A[(a, ll)]
    second = A[(b-2**ll+1, ll)]
    if test[first] <= test[second]:
        return first
    else:
        return second


for i in range(n):
    for j in range(i, n):
        print i,j, rmq(i,j)

