class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=len(nums)*[1]
        f=1
        for n in range(len(nums)):
            r[n]=f
            f*=nums[n]
        f=1
        for n in range(len(nums)-1,-1,-1):
            r[n]*=f
            f*=nums[n]
        return r