class Solution:
    def topKFrequent(self, x: List[int], k: int) -> List[int]:
        l={}
        s=[[] for n in range(len(x)+1)]
        for n in x:
            l[n]=1+l.get(n,0)
        for n,c in l.items():
            s[c].append(n)
        r=[]
        for n in reversed(s):
            r.extend(n)
            if len(r)==k:
                return r