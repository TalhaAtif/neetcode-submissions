class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diffs = {0:1}
        total = 0
        result = 0
        for i in range(len(nums)):
            total+=nums[i]
            diff = total - k
            if diff in diffs:
                result+=diffs[diff]
            diffs[total] = diffs.get(total,0) + 1
        return result