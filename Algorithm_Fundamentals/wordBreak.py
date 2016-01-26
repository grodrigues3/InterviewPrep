import pdb
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    q1 = [0]
    q2 = []
    n = len(s)
    visited = {}
    

    while True:
        for starting_point in q1:
            for word in wordDict:
                end = starting_point + len(word)
                if s[starting_point:end] == word:
                    if end == n:
                        return True
                    if end in visited:
                        continue
                    q2 += end,
                    visited[end] = True
        q1, q2 = q2, []
        if not q1 or min(q1) > n:
            return False


print wordBreak("dwordssanddeeds", ["word", 'sand', 'deeds', 'words'])
                
