class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for n in range(len(nums)):
            diff=target-nums[n]
            if diff in l:
                return [l[diff],n]
            l[nums[n]] = n