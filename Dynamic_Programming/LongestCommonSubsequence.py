'''
leetcode 1143

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

class Solution:
    def memoization(self,text1,text2,i,j,mat):
        if i == len(text1) or j == len(text2):
            return 0
        if mat[i][j]!=-1:
            return mat[i][j]
        if (text1[i] == text2[j]):
            mat[i][j] = 1 + self.memoization(text1,text2,i+1,j+1,mat)
            return mat[i][j]
        else:
            mat[i][j] = max(self.memoization(text1,text2,i+1,j,mat),self.memoization(text1,text2,i,j+1,mat))
            return mat[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = [[-1]*len(text2) for i in range(len(text1))]
        return self.memoization(text1,text2,0,0,mat)