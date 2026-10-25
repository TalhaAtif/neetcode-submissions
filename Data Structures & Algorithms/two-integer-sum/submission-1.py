class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2,3,6 5
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return [diffs[diff],i]
            diffs[nums[i]] = i
        return []