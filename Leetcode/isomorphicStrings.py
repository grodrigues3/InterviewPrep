"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = {}
        MAX_UNIQUE_CHARS = 1000
        already_mapped = [False]*MAX_UNIQUE_CHARS
        for i,char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[i]:
                    return False
            else:
                ind = ord(t[i])
                if already_mapped[ind] == True:
                    return False
                mapping[char] = t[i]
                already_mapped[ind] = True
        return True
