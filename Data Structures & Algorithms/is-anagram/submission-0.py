class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettersT = {}
        lettersS = {}
        for i in range(len(t)):
            lettersT[t[i]] = lettersT.get(t[i],0) + 1    
            lettersS[s[i]] = lettersS.get(s[i],0) + 1    
        return lettersS == lettersT