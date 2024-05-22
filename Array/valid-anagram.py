'''
leetcode-242
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = {}
        for character in s:
            if character in mapping:
                mapping[character] += 1
            else:
                mapping[character] = 1
        for character in t:
            if character in mapping:
                mapping[character] -= 1
            else:
                return False
        for char in mapping:
            if mapping[char]!=0:
                return False
        return True

