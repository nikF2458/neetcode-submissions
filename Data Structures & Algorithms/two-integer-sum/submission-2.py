class Solution:
    def twoSum(self, x: List[int], t: int) -> List[int]:
        l={}
        for n in range(len(x)):
            if t-x[n] in l:
                return [l[t-x[n]],n]
            l[x[n]] = n
        return []
