class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        tD = {}
        s = (list(s))
        t = (list(t))
        for ch in s:
            if ch in sD:
                sD[ch] += 1
            else:
                sD[ch] = 1
        for ch in t:
            if ch in tD:
                tD[ch] += 1
            else:
                tD[ch] = 1
        
        return sD == tD