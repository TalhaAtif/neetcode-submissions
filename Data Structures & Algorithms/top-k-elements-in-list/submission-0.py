class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            counts[i] = 1 + counts.get(i,0)
        for i, j in counts.items():
            freq[j].append(i)

        result = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result