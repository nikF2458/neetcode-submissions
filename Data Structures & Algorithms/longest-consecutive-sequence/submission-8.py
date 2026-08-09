class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=defaultdict(int)
        c=0
        for n in nums:
            if not l[n]:
                l[n]=l[n-1]+l[n+1]+1
                l[n-l[n-1]]=l[n]
                l[n+l[n+1]]=l[n]
                c=max(c,l[n])
        return c