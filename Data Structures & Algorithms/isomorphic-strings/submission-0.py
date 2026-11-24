class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letterMapS = {}
        letterMapT = {}
        
        for i in range(len(s)):
            if s[i] in letterMapS or t[i] in letterMapT:
                if letterMapS.get(s[i]) != t[i] or letterMapT.get(t[i]) != s[i]:
                    return False
            
            letterMapS[s[i]] = t[i]
            letterMapT[t[i]] = s[i]
            
        return True