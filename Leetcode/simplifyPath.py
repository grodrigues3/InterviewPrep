"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
__author__ = 'grodrigues'
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        myRes = []
        pieces = path.split("/")
        
        for p in pieces:
            if p:
                if p == "..":
                    if len(myRes) > 0:
                        myRes.pop()
                elif p != ".":
                    myRes.append(p)
        return "/" + "/".join(myRes)
