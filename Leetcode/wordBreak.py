"""
Word Break Problem
    Input:
        1. A string not separated with whitespace
        2. A dictionary
    Output:
        1. Boolean: Indicating whether the input string can be
            split into words from the dictionary
"""
__author__ = 'grodrigues'

def wordBreak(s, wordDict):
    if s == "":
        return True
        
    n = len(s)
    bool = [0 for x in range(n+1)]
    for i in range(1,n+1):
        if s[:i] in wordDict:
            bool[i] = 1
            
        if bool[i]:
            if i == n:
                return True
            for j in range(i+1, n+1):
                if s[i:j] in wordDict:
                    bool[j] = 1
                if j == n and bool[j] == 1:
                    return True
    return False


def testAlgorithm():
    sampleDict = ['hello', 'is', 'my', 'in', 'garrett', 'name', 'san', 'diego', 'lifestyle']
    testStr0='hellomynameisgarrett' #hello my name is garrett 
    testStr1='garrettlivesinsandiego' #garrett lives in san diego but "lives" is not in dict
    edgeCase = ""
    print 'Testing the algorithm on the following...'
    print "\n".join([testStr0, testStr1, edgeCase])
    assert wordBreak(testStr0, sampleDict) == True
    assert wordBreak(testStr1, sampleDict) == False
    assert wordBreak("", []) == True

if __name__ == "__main__":
    testAlgorithm()
    
