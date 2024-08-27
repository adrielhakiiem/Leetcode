class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # only anagram if the length of the words are the same 
        if len(s) != len(t):
            return False
        # sort the letters 
        s, t = sorted(s), sorted(t)
        # compare 
        if s == t:
            return True
        else:
            return False
