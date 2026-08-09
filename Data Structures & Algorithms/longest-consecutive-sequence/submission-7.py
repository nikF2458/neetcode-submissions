class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        l=set(nums)
        c=0
        for n in nums:
            if n-1 not in l:
                t=1
                while n+t in l:
                    t+=1
                c=max(c,t)
        return c