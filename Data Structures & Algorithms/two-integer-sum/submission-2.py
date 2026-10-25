class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums  = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in sums:
                return [sums[goal],i]
            sums[nums[i]] = i