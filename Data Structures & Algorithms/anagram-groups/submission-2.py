class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allCounts = {}
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')] += 1
            freq = tuple(freq)
            if freq in allCounts:
                allCounts[freq].append(s)
            else:
                allCounts[freq] = [s]
        return list(allCounts.values())